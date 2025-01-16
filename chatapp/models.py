from django.db import models
from django.contrib.auth.models  import User
import datetime

# Create your models here.
class Message(models.Model):
    sender=models.ForeignKey(User,related_name='sent_messages',on_delete=models.CASCADE)
    receipent=models.ForeignKey(User,related_name='received_messages',on_delete=models.CASCADE)
    message=models.TextField(max_length=100)
    timestamp=models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return f'Message from: {self.sender} to {self.receipent}'
    
    
    