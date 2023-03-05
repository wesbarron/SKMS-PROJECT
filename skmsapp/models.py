from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, choices= (('User','User'), ('Expert','Expert'), ('RiskManager','RiskManager')), default='User')
    userimage = models.ImageField(null=True, blank=True, upload_to="images/profile/")

    def __str__(self):
        return str(self.user)