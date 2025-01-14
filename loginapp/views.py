from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from .models import *

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
    return render(request,'services.html',{})

def contacts_page(request):
    return render(request,'Contacts.html',{}) 

def chatbot_page(request):
    return render(request,'chatbot.html',{})

       
       
       
       
#Dashboard view (after login)

@login_required
def dashboard_view(request):
    return render(request,'newbg.html',{})

#Logout view
def logout_view(request):
    logout(request)
    messages.success(request,("You have been logged out successfully "))
    return redirect("login")       



def pneumonia_div(request):
    return render(request,'pneumoniadiv.html',{})
