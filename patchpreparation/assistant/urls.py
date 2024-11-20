from django.urls import path

from . import views

app_name = "assistant"
urlpatterns = [
    path("", views.index, name="index"),
    path("preview/", views.preview, name="preview"),
    path("generate/", views.generate, name="generate"),
]