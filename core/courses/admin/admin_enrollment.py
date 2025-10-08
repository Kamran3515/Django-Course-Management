from django.contrib import admin
from ..models import *

# Register your models here.
@admin.register(Enrollment)
class AdminEnrollment(admin.ModelAdmin):
    list_display = ("id" ,"user" ,"course" ,"created_at" ,"updated_at")