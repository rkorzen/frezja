from django.urls import path

from . import views

app_name = "home"  # posts:list
urlpatterns = [
    path("", views.home, name="home"),
]
