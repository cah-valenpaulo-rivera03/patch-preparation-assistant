import os
import json
import datetime

import calendar

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
    week=[
        {
            "title": "Non-Prod Week",
            "header": "Generate Server List",
            "changes": [
                {
                    "title": "Change #1",
                    "name": "change1",
                    "patchTags": [
                        "patch-flexible-stage-sap-gsc-secondary-app1",
                        "patch-flexible-stage-sap-tpm-secondary-manual"
                    ]
                },
                {
                    "title": "Change #2",
                    "name": "change2",
                    "patchTags": [
                        "patch-day-03-at-0000-stage",
                        "patch-day-03-at-0100-stage",
                        "patch-day-03-at-0900-stage",
                        "patch-day-03-at-1200-stage-sap-china",
                        "patch-day-03-at-1300-stage",
                        "patch-day-03-at-1400-stage",
                        "patch-day-03-at-2000-stage",
                        "patch-day-03-at-2100-stage",
                        "patch-day-04-at-0200-stage",
                        "patch-day-04-at-0900-stage-datamarket",
                        "patch-day-04-at-2000-stage",
                        "patch-day-04-at-2100-stage",
                        "patch-day-04-at-2100-stage-b2bi",
                        "patch-day-04-at-2200-stage",
                        "patch-day-04-at-2300-stage-b2bi",
                        "patch-day-05-at-2100-stage",
                        "patch-day-05-at-2300-stage-b2bi",
                        "patch-flexible-stage-sap-gsc-primary-app2",
                        "patch-flexible-stage-sap-singapore",
                        "patch-flexible-stage-sap-tpm-primary"
                    ]
                },
                {
                    "title": "Change #3",
                    "name": "change3",
                    "patchTags": [
                        "patch-flexible-stage-pds-dr-secondary-manual",
                        "patch-flexible-stage-pds-primary-manual",
                        "patch-flexible-stage-sap-nphs-primary-app2",
                        "patch-flexible-stage-sap-nphs-secondary-app1"
                    ]
                },
                {
                    "title": "Change #4",
                    "name": "change4",
                    "patchTags": [
                        "patch-flexible-prod-sap-gsc-secondary-dr-app1",
                    ]
                }
            ]
        },
        {
            "title": "Prod Week 1",
            "header": "Generate Server List",
            "changes": [
                {
                    "title": "Change #1",
                    "name": "change1",
                    "patchTags": [
                        "patch-day-11-at-1600-prod-df",
                        "patch-day-11-at-1600-prod-sap-china",
                        "patch-day-11-at-2100-prod",
                        "patch-day-11-at-2100-prod-b2bi",
                        "patch-day-11-at-2300-prod-b2bi",
                        "patch-day-12-at-0000-prod",
                        "patch-day-12-at-2300-prod-b2bi",
                        "patch-flexible-prod-3pl",
                        "patch-flexible-prod-hci-manual",
                        "patch-flexible-prod-matillion-manual",
                        "patch-flexible-prod-medical-mq",
                        "patch-flexible-prod-sap-gsc-primary-app2",
                        "patch-flexible-prod-sap-singapore",
                        "patch-flexible-prod-sap-tpm-primary-app2",
                        "patch-flexible-prod-sap-tpm-secondary-dr-app1"
                    ]
                },
                {
                    "title": "Change #2",
                    "name": "change2",
                    "patchTags": [
                        "patch-flexible-stage-pmod2",
                        "patch-flexible-stage-sap-corp",
                        "patch-flexible-stage-sap-pharma-primary-app",
                        "patch-flexible-stage-sap-pharma-secondary"
                    ]
                },
                {
                    "title": "Change #3",
                    "name": "change3",
                    "patchTags": [
                        "patch-flexible-prod-sap-nphs-secondary-app1",
                    ]
                }
            ]
        },
        {
            "title": "Prod Week 2",
            "header": "Generate Server List",
            "changes": [
                {
                    "title": "Change #1",
                    "name": "change1",
                    "patchTags": [
                        "patch-day-17-at-0000-prod",
                        "patch-day-18-at-0200-prod",
                        "patch-day-18-at-0300-prod",
                        "patch-day-18-at-0300-prod-sas",
                        "patch-day-18-at-0900-prod-datamarket",
                        "patch-day-18-at-1500-prod-canada",
                        "patch-day-18-at-1630-prod-chromeleon",
                        "patch-day-18-at-1800-prod",
                        "patch-day-18-at-2000-prod",
                        "patch-day-18-at-2000-prod-canada",
                        "patch-day-18-at-2100-bi-monthly-prod-kalik",
                        "patch-day-18-at-2100-prod",
                        "patch-day-18-at-2100-prod-Automic",
                        "patch-day-18-at-2100-prod-canada",
                        "patch-day-18-at-2200-prod",
                        "patch-day-18-at-2300-prod",
                        "patch-day-18-at-2300-prod-cim",
                        "patch-day-19-at-0000-prod",
                        "patch-day-19-at-0200-prod",
                        "patch-day-19-at-0300-prod-maximo",
                        "patch-day-19-at-0600-prod",
                        "patch-day-19-at-0600-prod-infosphere",
                        "patch-day-19-at-2000-prod",
                        "patch-day-19-at-2100",
                        "patch-day-19-at-2100-prod",
                        "patch-day-19-at-2100-prod-Automic",
                        "patch-day-19-at-2100-prod-canada",
                        "patch-day-19-at-2200-prod",
                        "patch-day-19-at-2300-prod",
                        "patch-flexible-prod-aro-even",
                        "patch-flexible-prod-aro-odd",
                        "patch-flexible-prod-pds-dr-secondary-manual",
                        "patch-flexible-prod-pds-primary-manual",
                        "patch-flexible-prod-sap-nphs-primary-app2"
                    ]
                },
                {
                    "title": "Change #2",
                    "name": "change2",
                    "patchTags": [
                        "patch-day-20-at-0300-prod-moms-day1",
                        "patch-day-20-at-1100-prod",
                        "patch-day-21-at-0300-prod-moms-day2"
                    ]
                },
                {
                    "title": "Change #3",
                    "name": "change3",
                    "patchTags": [
                        "patch-day-23-at-1100-prod",
                    ]
                }
            ]
        },
        {
            "title": "Prod Week 3",
            "header": "Generate Server List",
            "changes": [
                {
                    "title": "Change #1",
                    "name": "change1",
                    "patchTags": [
                        "patch-day-25-at-2000-prod",
                        "patch-day-25-at-2100-prod",
                        "patch-day-25-at-2100-prod-sap-pharma",
                        "patch-day-25-at-2200-prod",
                        "patch-day-25-at-2200-prod-manhattan",
                        "patch-day-25-at-2200-prod-pmod2-manhattan",
                        "patch-day-26-at-0000-prod",
                        "patch-day-26-at-0000-prod-ecm",
                        "patch-day-26-at-0000-prod-manhattan",
                        "patch-day-26-at-0100-prod-pmod2-manhattan",
                        "patch-day-26-at-0200-prod",
                        "patch-day-26-at-0400-prod-ecm",
                        "patch-day-26-at-2000-prod",
                        "patch-day-26-at-2100-prod",
                        "patch-flexible-prod-ecm-even-manual",
                        "patch-flexible-prod-ecm-odd-manual",
                        "patch-flexible-prod-pmod2",
                        "patch-flexible-prod-sap-corp",
                        "patch-flexible-prod-sap-pharma-ph1-manual",
                        "patch-flexible-prod-sap-pharma-pk1-manual",
                        "patch-flexible-prod-sap-pharma-primary-app",
                        "patch-flexible-prod-sap-pharma-secondary"
                    ]
                }
            ]
        }
    ]
    context = week[patchingWeek]
    
    return render(request, "assistant/preview.html", context)

def generate(request):
    patchServerCollectionData = request.FILES["filename"]

    with open(source_file, "wb+") as destination:
        for line in patchServerCollectionData.chunks():
            destination.write(line)

    os.system("rm -rf output/*.csv")
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

    for keyword in patch_tags:
        with open(source_file, "r") as csvfile:
            for line in csvfile:
                patch_tag = line.split(",")[2]
                if (keyword == patch_tag and exempt_tag not in line):                    
                    with open(filename, "a") as destination:
                        destination.write(line)

def get_patch_cycle():
    # get current date
    today = datetime.datetime.now()
    month = today.month
    day = today.day
    year = today.year

    patch_tuesday = get_patch_tuesday(month, year)

    if day > patch_tuesday.day:
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
