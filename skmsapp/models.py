from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, choices= (('User','User'), ('Expert','Expert'), ('RiskManager','RiskManager')), default='User')
    userimage = models.ImageField(null=True, blank=True, upload_to="images/profile/")

    def __str__(self):
        return str(self.user)

class Report(models.Model):
    reporter_comments = models.TextField()
    reporter_name = models.CharField(max_length=300, choices= (('Current User','Current User'), ('Anonymous','Anonymous')), default='Current User')
    report_date = models.DateTimeField(auto_now_add=True)
    contact_preference = models.CharField(max_length = 3, choices= (('N','No'), ('Y','Yes')), default='Y')
    report_anonymously = models.CharField(max_length = 3, choices= (('N','No'), ('Y','Yes')), default='N')
    submitter = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.report_date)

class Voice(models.Model):
    voice_comments = models.TextField()
    voice_user = models.CharField(max_length=300, choices= (('Current User','Current User'), ('Anonymous','Anonymous')), default='Current User')
    voice_date = models.DateTimeField(auto_now_add=True)
    contact_preference = models.CharField(max_length = 3, choices= (('N','No'), ('Y','Yes')), default='Y')
    voice_anonymously = models.CharField(max_length = 3, choices= (('N','No'), ('Y','Yes')), default='N')
    submitter = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.voice_date)

class Post(models.Model):
    #likes, comments, title, content, userUploaded, date, time, subject, subscriptions
    title = models.CharField(max_length=200)
    content = models.TextField()
    #author = models.ForeignKey('skmsapp.UserProfile', on_delete=models.CASCADE)
    author = models.CharField(max_length=300)
    author_type = models.CharField(max_length=20, null=True)
    datetime = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    subject = models.CharField(max_length=100, choices= (('Asset','Asset'), ('Counter Measure','Counter Measure'), ('Threat','Threat'), ('Vulnerability','Vulnerability')))
    subscriptions = models.ManyToManyField('skmsapp.UserProfile', related_name='subscribed_posts')
    comments = models.ManyToManyField('Comment', related_name='post_comments')
    
    def __str__(self):
        return self.subject

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    #author = models.ForeignKey('skmsapp.UserProfile', on_delete=models.CASCADE)
    author = models.CharField(max_length=300)
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} - {self.content}'

class ReportReplyToSubmitter(models.Model):
    submitter = models.CharField(max_length=50, null=True)
    report_reply = models.TextField()
    reply_date = models.DateTimeField(auto_now_add=True)
    activity_date = models.DateTimeField(null=True)
    is_read = models.CharField(max_length=1)

    def __str__(self):
        return f'{self.submitter} - {self.activity_date}'

class Asset(models.Model):
    assetid = models.AutoField(db_column='AssetID', primary_key=True)  # Field name made lowercase.
    assetname = models.TextField(db_column='AssetName', unique=True)  # Field name made lowercase.

    def __str__(self):
        return self.assetname

class CountermeasureDescription(models.Model):
    countermeasureid = models.OneToOneField('Countermeasure', models.DO_NOTHING, db_column='CounterMeasureID', primary_key=True)  # Field name made lowercase.
    countermeasuredescription = models.TextField(db_column='CounterMeasureDescription')  # Field name made lowercase.

    def __str__(self):
        return self.countermeasuredescription

class Countermeasure(models.Model):
    countermeasureid = models.AutoField(db_column='CounterMeasureID', primary_key=True)  # Field name made lowercase.
    countermeasurename = models.TextField(db_column='CounterMeasureName', unique=True)  # Field name made lowercase.

    def __str__(self):
        return self.countermeasurename

class ThreatDescription(models.Model):
    threatid = models.OneToOneField('Threat', models.DO_NOTHING, db_column='ThreatID')  # Field name made lowercase.
    threatdescription = models.TextField(db_column='ThreatDescription')  # Field name made lowercase.

    def __str__(self):
        return self.threatdescription

class Threat(models.Model):
    threatid = models.AutoField(db_column='ThreatID', primary_key=True)  # Field name made lowercase.
    threatname = models.TextField(db_column='ThreatName', unique=True)  # Field name made lowercase.

    def __str__(self):
        return self.threatname
