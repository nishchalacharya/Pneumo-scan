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

# #Login Views

# def login_view(request):
#     if request.method=="POST":
#         form=LoginForm(request.POST)
#         if form.is_valid():
#             username=form.cleaned_data['username']
#             password=form.cleaned_data['password'] 
#             user=authenticate(request,username=username,password=password)
#             if user is  not None:
#                 login(request,user)
#                 return redirect('dashboard')
#             else:
#                 messages.error(request,"Invalid Username or password.Please try again.")
#     else:
#         form=LoginForm()
#     return render(request,'login.html',{'form':form})     




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
    return render(request,'Contacts.html',{}) 

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




# def pneumonia_div(request):
#     """Handles file upload, makes predictions, and renders results."""
#     if request.method == "POST":
#         # Get the uploaded image file
#         image_file = request.FILES.get("xray_image")  # Match name in HTML form
#         if not image_file:
#             return JsonResponse({"error": "No image uploaded"}, status=400)

#         # Save the uploaded image instance
#         xray_instance = Xrayimage(xray_image=image_file)
#         xray_instance.save()

#         # Save image path for processing
#         image_path = xray_instance.xray_image.path  # Path to the saved image file

#         # Make prediction using the model
#         result = predict_images(image_path)

#         # Render the result page with prediction
#         return render(request, "uploadfile.html", {
#             "result": result  # Pass the prediction result to the template
#         })

#     # For GET requests, just render the form
#     return render(request, "uploadfile.html")

      
            
           
         






    



# densenet_model=joblib.load('')

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
      
        
           
    


def view_profile(request):
    
    return render(request,'myprofile.html',{})


class  BlogHome(ListView):
    model=blog_post
    template_name='blog_home.html'
    ordering=['-post_date']
    
    
    
class detailblogview(DetailView):
    model=blog_post
    template_name='blogdetail.html'    
    
    
    
class AddPostview(CreateView):
    model=blog_post
    template_name='addblog_post.html'    
    fields = '__all__'
    
    
    
    
# ------------------------------------------------------------------------- esparsh ml 


# import os
# import numpy as np
# import tensorflow as tf
# import cv2
# from django.shortcuts import render
# from django.conf import settings

#  # Assuming you have a form for uploading images
# from PIL import Image
# from django.core.files.storage import default_storage
# from django.core.files.base import ContentFile






# # Create a function to preprocess images for prediction
# def preprocess_image(image_file):
#     # Open the image using PIL
#     img = Image.open(image_file)
#     # Resize the image to match the input size expected by the model (224x224)
#     img = img.resize((224, 224))
#     # Convert image to numpy array
#     img = np.array(img)
#     # Convert from RGB to BGR (since OpenCV uses BGR)
#     img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
#     # Normalize the image to [0, 1] range
#     img = img / 255.0
#     # Add an extra dimension to match the model input shape (batch size)
#     img = np.expand_dims(img, axis=0)
#     return img

# # Prediction view to handle image upload and model prediction
# def ulcer_detection_view(request):
#     if request.method == 'POST' and request.FILES.get('image'):
#         uploaded_image = request.FILES['image']
        
#         # Preprocess the image for prediction
#         image = preprocess_image(uploaded_image)
        
#         # Predict using the trained model
#         prediction = model.predict(image)
        
#         # Determine result based on prediction
#         result = 'Ulcer' if prediction[0][0] > 0.5 else 'No Ulcer'
        
#         # Save the uploaded image temporarily to display it
#         image_path = default_storage.save(f'uploads/{uploaded_image.name}', ContentFile(uploaded_image.read()))
#         image_url = default_storage.url(image_path)

#         # Return the result and image URL to the template
#         return render(request, 'result.html', {'result': result, 'image_url': image_url})

#     # If GET request or invalid image, render the image upload form
#     return render(request, 'upload.html')