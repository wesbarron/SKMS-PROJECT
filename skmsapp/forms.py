from django import forms
from django.forms import ModelForm
from .models import Report, Voice, Post

class SubmitReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ('reporter_comments', 'reporter_name', 'contact_preference', 'report_anonymously')
        labels = {
            'reporter_comments': 'Describe the problem or issue in detail below:',
            'reporter_name': 'Name (Choose "Anonymous" if you do not wish to be identified)',
            'contact_preference': 'Do you wish to be contacted?',
            'report_anonymously': 'Would you like this report to be anonymous?',
        }
        widgets = {
            'reporter_comments': forms.Textarea(attrs={'class':'form-control'}),
            'reporter_name': forms.Select(attrs={'class':'form-control text-center'}),
            'contact_preference': forms.Select(attrs={'class':'form-control text-center'}),
            'report_anonymously': forms.Select(attrs={'class':'form-control text-center'}),
        }

class SubmitVoiceForm(ModelForm):
    class Meta:
        model = Voice
        fields = ('voice_comments', 'voice_user', 'contact_preference', 'voice_anonymously')
        labels = {
            'voice_comments': 'Describe the best practice or improvement in detail below:',
            'voice_user': 'Name (Choose "Anonymous" if you do not wish to be identified)',
            'contact_preference': 'Do you wish to be contacted?',
            'voice_anonymously': 'Would you like this report to be anonymous?',
        }
        widgets = {
            'voice_comments': forms.Textarea(attrs={'class':'form-control'}),
            'voice_user': forms.Select(attrs={'class':'form-control text-center'}),
            'contact_preference': forms.Select(attrs={'class':'form-control text-center'}),
            'voice_anonymously': forms.Select(attrs={'class':'form-control text-center'}),
        }

class SubmitPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'subject')
        labels = {
            'title': 'Title:',
            'content': 'Description',
            'subject': 'Subject (Select One)',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'subject': forms.Select(attrs={'class':'form-control text-center'}),
        }