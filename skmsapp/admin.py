from django.contrib import admin
from .models import *
from . import models

admin.site.register(UserProfile)
admin.site.register(models.Report)
admin.site.register(models.Voice)
admin.site.register(models.Comment)
admin.site.register(models.Post)
admin.site.register(models.ReportReplyToSubmitter)
admin.site.register(models.Asset)
admin.site.register(models.Countermeasure)
admin.site.register(models.CountermeasureDescription)
admin.site.register(models.Threat)
admin.site.register(models.ThreatDescription)


