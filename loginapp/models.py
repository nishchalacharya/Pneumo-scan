from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from  datetime import datetime,date
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    phoneno=models.TextField(blank=True,null=True)
    is_doctor=models.BooleanField(default=False)
    profile_pic=models.ImageField(upload_to='profile_pictures/',default='media/profile_pictures/default.png',blank=True)
    
    
    def __str__(self):
        return f'{self.user.username} and is doctor: {self.is_doctor}'
    
    
    
class blog_post(models.Model):
    title=models.CharField(max_length=50)
    body=models.CharField(max_length=100)
    author =models.ForeignKey(User,on_delete=models.CASCADE)
    post_date=models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return f'{self.author} and {self.title}'
    
    def get_absolute_url(self):
        return reverse("detailblogview",args=(str(self.id)) )
    
    
    
class xray_image(models.Model):
    xray_image=models.ImageField(upload_to='x_rays_uploaded/',blank=False) 
    # xray_author=models.ForeignKey(Profile,on_delete=models.CASCADE)   
    
    # def __str__(self):
    #     return f'{self.xray_author}'
    
    
    
class contact_us(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)    
    message=models.TextField(max_length=100)
    
    def __str__(self):
        return f'{self.name}'
    
    
    
    
    
    
    
    
    
    
    
    
    