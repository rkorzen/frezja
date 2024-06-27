from django.contrib import admin
from .models import UserInquiry

# Register your models here.


# @admin.register(UserInquiry)
class UserInquiryAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "message", "created_at", "is_resolved"]
    list_filter = ["is_resolved"]
    search_fields = ["name", "email", "message"]


admin.site.register(UserInquiry, UserInquiryAdmin)
