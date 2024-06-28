from django.urls import path

from . import views

app_name = "photos"  # posts:list
urlpatterns = [
    path("", views.list, name="list"),
    path("galleries", views.galleries, name="galleries"),
    path("galleries/create", views.create_gallery, name="create-gallery"),
    path("galleries/<int:pk>", views.gallery, name="gallery"),
    path("create", views.create, name="create"),
    path("<int:pk>", views.details, name="details"),
]
