from django.urls import path

from . import views

app_name = "photos"  # posts:list
urlpatterns = [
    path("", views.list, name="list"),
    path("<int:pk>", views.details, name="details"),
]
