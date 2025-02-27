import os
import glob
import json
import datetime

import calendar

from patchtags.patchtags import week

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from datetime import timedelta

# Create your views here.

source_file="patchpreparation/assistant/static/patchServerCollection.csv"
 
def index(request):
    context = {
        "title": "Homepage",
        "header": "Generate Server List",
        "patchingWeeks": [
            {
                "id": "nonprod",
                "value": "0",
                "label": "Non-Prod"
            },
            {
                "id": "prod-1",
                "value": "1",
                "label": "Prod Week 1"
            },
            {
                "id": "prod-2",
                "value": "2",
                "label": "Prod Week 2"
            },
            {
                "id": "prod-3",
                "value": "3",
                "label": "Prod Week 3"
            }
        ]
    }

    return render(request, "assistant/index.html", context)

def preview(request):
    patchingWeek = int(request.POST["patchingWeek"])
    context = week[patchingWeek]
    
    return render(request, "assistant/preview.html", context)

def generate(request):
    patchServerCollectionData = request.FILES["filename"]

    with open(source_file, "wb+") as destination:
        for line in patchServerCollectionData.chunks():
            destination.write(line)

    # os.system("rm -rf output/*.csv")
    for csv in glob.glob("output/*.csv"):
        os.remove(csv)
        
    for key in request.POST:
        if "change" in key:
            generate_list(key, request.POST.getlist(key))

    messages.success(request, "Server list has been generated")

    return HttpResponseRedirect(reverse("assistant:index"))

def generate_list(change, patch_tags):
    filename = "output/" + change + ".csv"
    cycle = get_patch_cycle()
    month = cycle.split()[0]
    year = cycle.split()[1]
    exempt_tag = "exempt-patch-%s-%s" % (month.lower(), year)

    print(exempt_tag)
    for keyword in patch_tags:
        with open(source_file, "r") as csvfile:
            for line in csvfile:
                patch_tag = line.split(",")[2]
                if (keyword == patch_tag.strip('\"') and exempt_tag not in line):                    
                    with open(filename, "a") as destination:
                        destination.write(line)
                elif ("pharma" in keyword and keyword in patch_tag.strip('\"')):
                    with open(filename, "a") as destination:
                        destination.write(line)

def get_patch_cycle():
    # get current date
    today = datetime.datetime.now()
    month = today.month
    day = today.day
    year = today.year

    patch_tuesday = get_patch_tuesday(month, year)

    if day >= patch_tuesday.day:
        patch_cycle = month
        patch_cycle_year = year
    else:
        patch_cycle, patch_cycle_year = get_previous_patch_cycle(month, year)

    month_name = calendar.month_name[patch_cycle]
    return "%s %s" % (month_name, patch_cycle_year)

def get_previous_patch_cycle(month, year):
    if month == 1:
        prev_month = 12 
        year -= 1
    else:
        prev_month = month - 1 
    
    return prev_month, year

def get_patch_tuesday(month, year):
    # set basedate to the 12th day of the month
    # 12th day of the month always falls on 2nd week 
    basedate = datetime.datetime.strptime(
        '{} 12 {} 12:00AM'.format(month, year),
        '%m %d %Y %I:%M%p'
    )

    dayoftheweek = basedate.weekday() + 1

    if dayoftheweek > 6:
        dayoftheweek = 0

    return basedate - timedelta(days=dayoftheweek) + timedelta(days=2)
