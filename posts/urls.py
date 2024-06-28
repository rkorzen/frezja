from django.urls import path

from . import views


app_name = "posts"  # posts:list
urlpatterns = [
    # path("", views.list, name="list"),
    path("", views.PostListView.as_view(), name="list"),
    # path("<int:pk>", views.details, name="details"),
    path("<int:pk>", views.PostDetailView.as_view(), name="details"),
    # path("create", views.create, name="create"),
    path("create", views.PostCreateView.as_view(), name="create"),
]
