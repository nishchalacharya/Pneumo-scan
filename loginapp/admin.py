from django.contrib import admin
from .models  import *

# Register your models here.


# class ProfileDetails(admin.ModelAdmin):
#     list_display=['username','email','is_doctor']
    
admin.site.register(Profile)    
admin.site.register(blog_post)
admin.site.register(xray_image)

admin.site.register(contact_us)