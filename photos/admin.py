from django.contrib import admin  # noqa: F401
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail

from .models import Photo, Gallery
# Register your models here.


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ["title", "created", "modified", "status", "thumbnail"]
    list_filter = ["status"]

    def thumbnail(self, obj):
        if obj.img:
            thumb = get_thumbnail(obj.img, "100")
            return mark_safe(f"<img src='{thumb.url}' />")
        return "----"

    thumbnail.short_description = "Thumbnail"



class GalleryPhotosInline(admin.TabularInline):
    model = Gallery.photos.through
    extra = 1
    readonly_fields = ('thumbnail',)
    # fields = ("photo", "thumbnail")

    def thumbnail(self, obj):
        if obj.img:
            thumb = get_thumbnail(obj.img, "100")
            return mark_safe(f"<img src='{thumb.url}' />")
        return "----"

    thumbnail.short_description = "Thumbnail"


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    exclude = ["photos"]
    inlines = [GalleryPhotosInline]