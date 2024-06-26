from django.contrib import admin  # noqa: F401
from .models import Photo
# Register your models here.

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass