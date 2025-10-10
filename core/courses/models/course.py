from django.db import models
from accounts.models import User
from datetime import datetime
from .category import *
from django.utils import timezone



class Course(models.Model):
    teacher = models.ForeignKey('accounts.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField(null=True)
    image = models.ImageField(upload_to='course/',null=True,blank=True)
    category = models.ManyToManyField('Category')
    status = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
