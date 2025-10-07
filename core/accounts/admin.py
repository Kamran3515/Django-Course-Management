from django.utils.html import format_html
from django.urls import reverse

from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ("id","email", "is_staff", "is_active","role","created_at",'view_profile_link')

    def view_profile_link(self, obj):
        try:
            profile = Profile.objects.get(user=obj)
            url = reverse('admin:accounts_profile_change', args=[profile.id])
            return format_html('<a href="{}">{}</a>', url, obj.email)
        except Profile.DoesNotExist:
            return "No profile"

    view_profile_link.short_description = "Profile"



@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ["id", "user","first_name", "last_name", "bio", "created_at"]
    list_display_links = ("user",)