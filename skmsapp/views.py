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
from .forms import *
import datetime



def home(request):
    return render(request, "home.html")

def userProfile(request):
    
    current_user = request.user
    user_profile = request.user.userprofile
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

def submitReport(request):
    submitted = False
    if request.method == 'POST':
        form = SubmitReportForm(request.POST) 
        userType = request.POST['reporter_name']
        if userType == 'Current User': 
            if form.is_valid():
                obj = form.save(commit=False)
                obj.submitter = request.user
                obj.save()
            return HttpResponseRedirect('/report?submitted=True')
        else:
            if form.is_valid():
                obj = form.save(commit=False)
                obj.submitter = 'Anonymous'
                obj.save()
    else:
        form = SubmitReportForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'report.html', {'form': form, 'submitted': submitted})

def submitVoice(request):
    submitted = False
    if request.method == 'POST':
        form = SubmitVoiceForm(request.POST)
        userType = request.POST['voice_user']
        if userType == 'Current User': 
            if form.is_valid():
                obj = form.save(commit=False)
                obj.submitter = request.user
                obj.save()
                return HttpResponseRedirect('/voice?submitted=True')
        else:
            if form.is_valid():
                obj = form.save(commit=False)
                obj.submitter = 'Anonymous'
                obj.save()
                return HttpResponseRedirect('/voice?submitted=True')
    else:
        form = SubmitVoiceForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'voice.html', {'form': form, 'submitted': submitted})

def viewReport(request, report_id):
    post = Report.objects.get(id=report_id)
    #user = UserProfile.objects.get(user=request.user.id)
    user = request.user
    if request.method == 'POST':
        content = request.POST["content"]
        datetime = timezone.now()
        NewReportReplyToSubmitter = ReportReplyToSubmitter(submitter=user, report_reply=content, is_read="N", activity_date=datetime)
        NewReportReplyToSubmitter.save()
        messages.success(request, "You're reply has been sent.'.")
        return redirect("viewAllReports")
    else:    
        return render(request, "view-reports.html", {'post':post, 'user':user})

def viewAllReports(request):
    post = Report.objects.values()
    user = request.user
    user_type = UserProfile.objects.filter(user=user, type="RiskManager").exists()
    if user_type == True:
        return render(request, "view-all-reports.html", {'post':post, 'user':user})
    else:
        messages.success(request, "You must have the Risk Management role to access this.")
        return redirect("home")

def viewVoice(request, voice_id):
    post = Voice.objects.get(id=voice_id)
    user = request.user
    if request.method == 'POST':
        content = request.POST["content"]
        datetime = timezone.now()
        NewReportReplyToSubmitter = ReportReplyToSubmitter(submitter=user, report_reply=content, is_read="N", activity_date=datetime)
        NewReportReplyToSubmitter.save()
        messages.success(request, "You're reply has been sent.'.")
        return redirect("viewAllReports")
    else:    
        return render(request, "view-voices.html", {'post':post, 'user':user})

def viewAllVoices(request):
    post = Voice.objects.values()
    user = request.user
    user_type = UserProfile.objects.filter(user=user, type="RiskManager").exists()
    if user_type == True:
        return render(request, "view-all-voices.html", {'post':post, 'user':user})
    else:
        messages.success(request, "You must have the Risk Management role to access this.")
        return redirect("home")

def createComment(request, post_id):
     if request.method == 'POST': 
        post = Post.objects.get(id=post_id)
        author = request.user
        content = request.POST['content']
        datetime = timezone.now()
        
        newComment = Comment(post=post, content=content, author=author, datetime=datetime)
        newComment.save()
        return redirect('post', post_id=post_id)

def createPost(request):
    if request.method == 'POST': 
        title = request.POST['title']
        content = request.POST['content'] 
        author = request.user
        author_type = author.userprofile.type
        datetime = timezone.now()
        subject = request.POST['subject']
        newPost = Post(title=title, content=content, author=author, author_type=author_type, datetime=datetime, subject=subject)
        newPost.save()
        return redirect('forum')

def post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "post.html", {'post':post})

def renderCreatePost(request):
    form = SubmitPostForm
    return render(request,"create-post.html", {'form':form})

def submitterReportList(request):
    post = ReportReplyToSubmitter.objects.values()
    user = request.user
    if user.is_authenticated:
            return render(request, "my-messages-list.html", {'post':post, 'user':user})
    else:
        messages.success(request, "You must be loged in to access your messages.")
        return redirect("home")

def readMessage(request, message_id):
    post = ReportReplyToSubmitter.objects.get(id=message_id)
    user = request.user
    if request.method == 'POST':
        is_read = request.POST['mark-read']
        if is_read == 'Y':
            post.delete()
            messages.success(request, "You have successfully deleted the last viewed message.")
            return redirect("submitterReportList")
        else:
            return redirect("submitterReportList")
    else:        
        return render(request, "my-messages-read.html", {'post':post, 'user':user})

def forum(request):
    current_user = request.user
    posts = Post.objects.all()
    if request.method == 'POST':
        category = request.POST['category']
        result = Post.objects.filter(subject=category).exists()
        if result == True:
            #posts = Post.objects.get(subject=category)
            posts = Post.objects.filter(subject=category).values()
            return render(request, 'discussion-home.html', {'current_user':current_user, 'current_user_id':current_user.id, 'posts':posts})
        else:
            if category == 'Categories':
                posts = Post.objects.all()
                return render(request, 'discussion-home.html', {'current_user':current_user, 'current_user_id':current_user.id, 'posts':posts})
            else:
                posts = Post.objects.all()
                return render(request, 'discussion-home.html', {'current_user':current_user, 'current_user_id':current_user.id})    
    else:
        return render(request, 'discussion-home.html', {'current_user':current_user, 'current_user_id':current_user.id, 'posts':posts})
