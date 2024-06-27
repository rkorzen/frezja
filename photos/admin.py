from django.contrib import admin  # noqa: F401
from .models import Photo, Gallery
# Register your models here.


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ["title", "created", "modified", "status"]
    list_filter = ["status"]

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', "modified"]
    # filter_horizontal = ["photos"]