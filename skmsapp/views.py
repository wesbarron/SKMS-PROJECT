from django.contrib.auth import forms  
from django.shortcuts import redirect, render  
from django.contrib import messages  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, "home.html")

def userProfile(request):
    
    current_user = request.user
    user_profile = request.user.userprofile
    #account_user = UserAccount.objects.filter(username__exact=current_user).values()
    if current_user.is_authenticated:
        #fs = FileSystemStorage()
        #uploaded_file_url = fs.url(account_user[0]['userimage'])
        context = {"current_user":current_user, "current_user_id":current_user.id, "firstname":current_user.first_name, "lastname":current_user.last_name, "email":current_user.email, "type":user_profile.type, }#"uploaded_file_url":uploaded_file_url}

        return render(request, 'user-profile.html', context=context)
    else:
        messages.success(request, "You need to be logged in to access this page.")
        return redirect("login")

def editProfile(request):
    current_user = request.user
    user_profile = request.user.userprofile
    context = {"current_user":current_user, "current_user_id":current_user.id, "firstname":current_user.first_name, "lastname":current_user.last_name, "email":current_user.email, "username":current_user, "type":user_profile.type,}
    if request.method == 'POST': 
        first_name = request.POST['firstname']
        last_name = request.POST['lastname'] 
        email = request.POST['email'] 
        username = request.POST['username']
        type = request.POST['type']
        userimage = request.FILES['userimage']
        fs = FileSystemStorage()
        filename = fs.save(userimage.name, userimage)
        uploaded_file_url = fs.url(filename)
        # context = {"uploaded_file_url":uploaded_file_url,"firstname":first_name, "lastname":last_name, "email":email, "current_user":username, "type":type}
        ins2 = User.objects.filter(username__exact=username).update(first_name=first_name, last_name=last_name, email=email, username=username)
        ins3 = UserProfile.objects.filter(user__exact=current_user.id).update(userimage=userimage)
        messages.success(request, "You're account has been successfully updated.")
        return redirect("userProfile")

    return render(request, 'edit-profile.html', context=context)