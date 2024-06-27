from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "author", "is_published"]
    list_filter = ["is_published"]
    search_fields = ["title", "content"]
