from django.contrib import messages
from django.shortcuts import redirect, render
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .scraper import ScrapeImages
import urllib.request
from django.http import FileResponse

@login_required(login_url="login")
def home(request):

    if request.method == "POST":
        url = request.POST.get("hero-field")  # fecthing url from input tag
        # validating inputted url
        if url.startswith("https") or url.startswith("http"):
            get_images = ScrapeImages(url)
            image_and_filename = get_images.get_all_images()
            return render(
                request,
                "home.html",
                context={"ImagesAndFilenames": image_and_filename},
            )
        # if invalid url then send error message
        else:
            messages.add_message(
                request, messages.INFO, "Wrong Website URL, Input with Protocols"
            )
            return redirect("extracting")  # redirect to home page
    return render(request, "home.html")  # rendering home page


def download():
    url = "https://i.pinimg.com/70x/df/b5/7e/dfb57e908aa08c86dba5ab81c1088c44.jpg"
    file=urllib.request.urlretrieve(url, "image.jpg")
    return file
    
 


def history(request):
    return render(request, 'history.html')

def help(request):
    return render(request, 'help1.html')



def Login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
             messages.error(
                request,"Username or Password is incorrect!!!"
            ) 
          

    return render (request,'login.html')
   
def signup(request):
     if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
      
        
        if '@' and '.' not in email:
             messages.error(
                request, "Enter valid Email"
            ) 
            
        else:
             if pass1 != pass2:
                messages.error(
                request, "Your password and confrom password are not Same!!" ) 
             else:

               my_user=User.objects.create_user(uname,email,pass1)
               my_user.save()
               return redirect('login')

       
     return render (request,'signup.html')


def Logout(request):
    logout(request)
    return redirect('login')

