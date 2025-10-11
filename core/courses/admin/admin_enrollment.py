from django.utils.html import format_html
from django.urls import reverse
from django.contrib import admin
from ..models import *

# Register your models here.
@admin.register(Enrollment)
class AdminEnrollment(admin.ModelAdmin):
    list_display = ("id" ,"student" ,"course" ,"enrolled_at","view_user_link")

    def view_user_link(self, obj):
        user = obj.course
        url = reverse('admin:accounts_user_change', args=[user.id])
        return format_html('<a href="{}">{}</a>', url, user.teacher)

    view_user_link.short_description = "Teacher Email"