from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from skmsapp.models import UserProfile 

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in, please check your credentials and try again.")
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            type = 'User'
            user = authenticate(username=username, password=password)
            UserProfile.objects.create(user=user, type=type)
            login(request, user)
            messages.success(request, "You have successfully been registered.")
            return redirect('home')
    else:
        form = RegisterUserForm()    
    return render(request, 'authenticate/register_user.html', {'form':form,})

