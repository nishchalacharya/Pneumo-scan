from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.TextField(blank=True,null=True)
    is_doctor=models.BooleanField(default=False)
    profile_pic=models.ImageField(upload_to='profile_pictures/',default='profile_pictures/default.jpg',blank=True)
    
    
    def __str__(self):
        return f'{self.user.username} and is doctor: {self.is_doctor}'
