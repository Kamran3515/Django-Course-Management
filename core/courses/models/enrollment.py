from django.db import models
from accounts.models import *
from .course import *

class Enrollment(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE,related_name='enrollments',null=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.email} ({self.student.role})"
    
    class Meta:
        unique_together = ('student', 'course')  # جلوگیری از ثبت‌نام تکراری
    
