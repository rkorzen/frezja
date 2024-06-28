from django.contrib import admin  # noqa: F401
from .models import Photo, Gallery
# Register your models here.


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ["title", "created", "modified", "status", "thumbnail"]
    list_filter = ["status"]


class GalleryPhotosInline(admin.StackedInline):
    model = Gallery.photos.through
    extra = 1

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    exclude = ["photos"]
    inlines = [GalleryPhotosInline]