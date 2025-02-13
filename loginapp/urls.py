
from django.urls import path,include
# from .views import *
from . import views
from .views import *


urlpatterns = [
    # path("accounts/", include("django.contrib.auth.urls")),
    path('register/',views.registration_view,name='registration'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('dashboard/',views.dashboard_view,name='dashboard'),
    
   
    path('services/',views.services_page,name='service_page'),
   
    path('chatbot/',views.chatbot_page,name="chatbot_page"),
    path('pneumoniadiv/',views.pneumonia_div,name='pneumonia_div'),
    # path("predictpneumonia/<int:image_id>/",views.predict_images,name="predict_pneumonia"),
    path('update_profile/',views.update_profile,name='profile_edit'),
    path('profile_view/',views.view_profile,name='profile_view'),
    path('homeblog/',BlogHome.as_view(),name='bloghome'),
    path('article_detail/<int:pk>',detailblogview.as_view(),name='detailblogview'),
    path('addpost/',AddPostview.as_view(),name='addpost')
    
    
    
]