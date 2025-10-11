from django.urls import path, include
from .views import *

app_name = "courses"

urlpatterns = [
    path("api/v1/", include("courses.api.v1.urls")),
]
