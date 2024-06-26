from django.contrib import admin
from .models import Tag

# Register your models here.


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    # readonly_fields = ["slug"]
    prepopulated_fields = {"slug": ("name",)}
