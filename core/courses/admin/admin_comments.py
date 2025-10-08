from django.contrib import admin
from ..models import *

# Register your models here.
@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ("id" ,"title" ,"body" ,"user" ,"course" ,"created_at" ,"updated_at")