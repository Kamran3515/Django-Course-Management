from django.db import models
from .users import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    bio = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='profiles/',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile of {self.user.email}"
    
@receiver(post_save, sender=User)
def save_profile(sender ,instance ,created ,**kwargs):
    if created:
        Profile.objects.create(user=instance)