from django.contrib import admin
from ..models import *

# Register your models here.
@admin.register(Lesson)
class AdminLessons(admin.ModelAdmin):
    list_display = ("id" ,"title" ,"body" ,"course" ,"status" ,"created_at" ,"updated_at")