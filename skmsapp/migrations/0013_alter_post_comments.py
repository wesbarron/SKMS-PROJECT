# Generated by Django 4.1.6 on 2023-03-06 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skmsapp', '0012_alter_post_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(null=True, related_name='post_comments', to='skmsapp.comment'),
        ),
    ]
