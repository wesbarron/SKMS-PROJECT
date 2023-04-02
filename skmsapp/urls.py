from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    # path('index/', views.index, name='index'),
    # path('sign-up/', views.createAccount),
    path('user-profile/', views.userProfile, name="userProfile"),
    path('forum/', views.forum, name='forum'),
    path('edit-profile/', views.editProfile, name="editProfile"),
    path('create-post/', views.renderCreatePost, name='createPost'),
    path('create/', views.createPost, name='create'),
    path('post/<int:post_id>/', views.post, name='post'),
    path('submit-comment/<int:post_id>', views.createComment, name='create-comment'),
    path('report/', views.submitReport, name='submitReport'),
    path('voice/', views.submitVoice, name='submitVoice'),
    path('view-reports/<int:report_id>/', views.viewReport, name='viewReports'),
    path('view-all-reports/', views.viewAllReports, name='viewAllReports'),
    path('view-voices/<int:voice_id>/', views.viewVoice, name='viewVoices'),
    path('view-all-voices/', views.viewAllVoices, name='viewAllVoices'),
    path('my-messages-list/', views.submitterReportList, name='submitterReportList'),
    path('my-messages-read/<int:message_id>/', views.readMessage, name='readMessages'),
    path('subject/<str:subject>/', views.subject, name='subject'),
    path('subject-description/<int:id>/', views.subjectDescription, name='subjectDescription'),
    path('dashboard/', views.dashboard, name='dashboard'),
    #path('login', auth_views.LoginView.as_view(template_name='skms/login.html'), name='login'),
    #path('logout', auth_views.LogoutView.as_view(template_name='skms/logout.html'), name='logout'),
]
