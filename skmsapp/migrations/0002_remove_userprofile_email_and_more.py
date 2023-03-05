# Generated by Django 4.1.7 on 2023-03-05 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skmsapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='password',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='status',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='username',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='type',
            field=models.CharField(choices=[('User', 'User'), ('Expert', 'Expert'), ('RiskManager', 'RiskManager')], default='User', max_length=255),
        ),
    ]