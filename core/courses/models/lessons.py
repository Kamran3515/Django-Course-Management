from django.db import models
from .course import *

class Lesson(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField(null=True)
    image = models.ImageField(upload_to='course/lesson/',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Lessons of {self.course.title}"