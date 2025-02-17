from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from .models import *
from django.views.generic import ListView,DetailView,CreateView
from django.http import HttpResponse,JsonResponse
import joblib
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import os

# Create your views here.


#Registation Form

def registration_view(request):
    form=UserRegisterForm()
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"Registration Successful")
            return redirect('login')
        
        else:
            messages.error(request,"Please,correct the errror below.")
    else:
        form=UserRegisterForm()
    return  render(request,'signup.html',{'form':form})

   




def login_view(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(username=username,password=password)
        
        if user is not None:
            login(request,user)
            messages.success(request,('You have been logged in succesfully.'))
            return redirect('dashboard')
        else:
            messages.success(request,('There was an error,Please try again...'))
            return redirect('login')       
    else:           
        return render(request,'login.html',{})
    
 
 
 
    
def about_page(request):
    return render(request,'about.html',{})
    

def services_page(request):
    return render(request,'uploadfile.html',{})

def contacts_page(request):
    if request.method=='POST':
        form=Feedbackpage(request.POST)
        if form.is_valid():
            form.save()
        else:
            return redirect('dashboard')
                
        
        
    return render(request,'index.html',{}) 

def chatbot_page(request):
    return render(request,'chatbot.html',{})

       
       
       
       
#Dashboard view (after login)

@login_required
def dashboard_view(request):
    return render(request,'index.html',{})

#Logout view
def logout_view(request):
    logout(request)
    messages.success(request,("You have been logged out successfully "))
    return redirect("login")       



from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import Xrayimage  # Ensure you have imported your form

def pneumonia_div(request):
    form=Xrayimage()
    result=None
    image_url=None
    if request.method == "POST": 
        # form = Xrayimage(request.POST, request.FILES['filepath'])
        form = Xrayimage(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            xray_instance = form.save(commit=False)
            xray_instance.save()
            image_url= xray_instance.xray_image.url #get image url
            #pass image to ML model for prediction
            print('image is passed to ml model')
            image_path=xray_instance.xray_image.path #get actual file path
            print("image uploaded successfuly",image_path)
            if os.path.exists(image_path):
                        print('image path exist')
                        result= predict_images(image_path)  
            else:
                        print('image path doesnt exist')                   
        else:
            print('form is not valid')  
            
        context={
                'form':form,
                'result':result,
                'image_url':image_url    
              }          
                
        print(f'context data are: {context}')
        return render(request,'uploadfile.html',context)
                           
    return render(request,'uploadfile.html',{'form':form})  




import tensorflow as tf
import numpy as np
from django.shortcuts import render
from django.http import JsonResponse
# from .models import Xrayimage






      
        
MODEL_PATH="./ai_models/densenet_finetuned.h5"
densenet_model=tf.keras.models.load_model(MODEL_PATH)




def predict_images(img_path):
    """Function to preprocess the image and make predictions using the ML model."""
    print('predict_image function is executed ')
    img = image.load_img(img_path, target_size=(224, 224))  # Adjust size to match model input
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0  # Normalize
    prediction = densenet_model.predict(img_array)[0][0]  # Adjust based on model output shape
    print('Model Loaded successfully')
    print(f'Prediction Value by fxn: {prediction}')
    return "Pneumonia Detected" if prediction > 0.5 else "Normal"
        
             
 
 
 
             
          
def update_profile(request):
    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
        else:
            form=ProfileForm(instance=request.user.profile)
    return render(request,'editprofile.html',{})    
      
        
           
    

@login_required
def view_profile(request):
    profile,created=Profile.objects.get_or_create(user=request.user) #fetch profile link to user and # auto creates if not exists
    return render(request,'myprofile.html',{'profile':profile})


class  BlogHome(ListView):
    model=blog_post
    template_name='blog.html'
    context_object_name = 'posts'
    ordering=['-post_date']
    
    
    
class detailblogview(DetailView):
    model=blog_post
    template_name='blogdetail.html'    
    
    
    
class AddPostview(CreateView):
    model=blog_post
    template_name='addblog_post.html'    
    fields = '__all__'
    
    
    

    
    
