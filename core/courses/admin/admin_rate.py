from django.contrib import admin
from ..models import *


# Register your models here.
@admin.register(Rate)
class AdminRate(admin.ModelAdmin):
    list_display = (
        "id",
        "score",
        "user",
        "course",
        "created_at",
        "updated_at",
    )
