from django.db import models
from datetime import datetime
from django.utils import timezone

from .course import *

class Lesson(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE, related_name='lesson')
    title = models.CharField(max_length=255)
    body = models.TextField(null=True)
    image = models.ImageField(upload_to='course/lesson/',null=True,blank=True)
    status = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Lessons of {self.course.title}"