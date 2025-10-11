from django.utils.html import format_html
from django.urls import reverse
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from ..models import *


# Register your models here.
@admin.register(User)
class AdminUser(BaseUserAdmin):
    model = User
    list_display = (
        "id",
        "email",
        "is_staff",
        "is_active",
        "role",
        "created_at",
        "view_profile_link",
    )
    list_filter = ("email", "is_staff", "is_active", "is_superuser")
    search_fields = ("email",)
    ordering = ("email",)
    fieldsets = (
        (
            "Authorisation",
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "role",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            "Create User",
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "role",
                ),
            },
        ),
    )

    def view_profile_link(self, obj):
        try:
            profile = Profile.objects.get(user=obj)
            url = reverse("admin:accounts_profile_change", args=[profile.id])
            return format_html('<a href="{}">{}</a>', url, profile.first_name)
        except Profile.DoesNotExist:
            return "No profile"

    view_profile_link.short_description = "Profile"
