from django.contrib import admin
from .models import UserProfile
from . import models

admin.site.register(UserProfile)
admin.site.register(models.Report)
admin.site.register(models.Voice)
admin.site.register(models.Comment)
admin.site.register(models.Post)
admin.site.register(models.ReportReplyToSubmitter)

