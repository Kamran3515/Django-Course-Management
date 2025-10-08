from django.contrib import admin
from ..models import *

# Register your models here.
@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ("id" ,"name" ,"created_at" ,"updated_at")