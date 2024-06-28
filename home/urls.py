from django.urls import path
from django.views.generic.base import TemplateView
from . import views

app_name = "home"  # posts:list
urlpatterns = [
    path("", views.home, name="home"),
    path("check/", views.check_spelling, name="check"),
    path("contact/", views.contact, name="contact"),
    # path("about/", views.about, name="about"),
    path("about/", TemplateView.as_view(template_name="about.html"), name="about"),
]
