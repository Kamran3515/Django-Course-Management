from django.contrib import admin
from ..models import *

# Register your models here.
@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ("id" ,"title" ,"body" ,"created_at" ,"updated_at")