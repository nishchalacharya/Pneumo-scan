
from django.urls import path,include
# from .views import *
from . import views

urlpatterns = [
    # path("accounts/", include("django.contrib.auth.urls")),
    path('register/',views.registration_view,name='registration'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('dashboard/',views.dashboard_view,name='dashboard'),
    path('about/',views.about_page,name='about_page'),
    path('services/',views.services_page,name='service_page'),
    path('contacts/',views.contacts_page,name='contact_page'),
    path('chatbot/',views.chatbot_page,name="chatbot_page"),
    path('pneumoniadiv/',views.pneumonia_div,name='pneumonia_div'),
    path('update_profile/',views.update_profile,name='profile')
    
    
]