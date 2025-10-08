from django.utils.html import format_html
from django.urls import reverse
from django.contrib import admin
from ..models import *

# Register your models here.
@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ("id","user", "first_name", "last_name", "bio", "created_at", "view_user_link")

    def view_user_link(self, obj):
        user = obj.user
        url = reverse('admin:accounts_user_change', args=[user.id])
        return format_html('<a href="{}">{}</a>', url, user.email)

    view_user_link.short_description = "User Email"