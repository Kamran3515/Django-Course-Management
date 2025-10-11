from django.contrib import admin
from ..models import *

# Register your models here.
@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ("id" ,"title" ,"body" ,"teacher" ,"status" ,"published_at" ,"created_at" ,"updated_at")
    search_fields =['title']