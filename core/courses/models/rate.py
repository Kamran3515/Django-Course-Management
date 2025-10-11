from django.db import models
from django.core.validators import MaxValueValidator
from accounts.models import User
from .course import *


class Rate(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="rate"
    )
    course = models.OneToOneField(
        Course, on_delete=models.CASCADE, related_name="rate"
    )
    score = models.PositiveIntegerField(validators=[MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email} ({self.user.role})"
