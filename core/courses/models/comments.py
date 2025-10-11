from django.db import models
from accounts.models import User
from .course import Course

class Comment(models.Model):
    user = models.ForeignKey('accounts.User',on_delete=models.CASCADE, related_name='comment')
    course = models.ForeignKey('Course',on_delete=models.CASCADE, related_name='comment')
    comment = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile of {self.user.email}"