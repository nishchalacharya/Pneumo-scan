

from django.urls import path,include
from django.shortcuts import render



urlpatterns = [
   
    path('chat/', lambda request: render(request, 'chat.html')),
]