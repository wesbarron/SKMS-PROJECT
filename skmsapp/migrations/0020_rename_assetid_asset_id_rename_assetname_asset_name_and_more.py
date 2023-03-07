# Generated by Django 4.1.6 on 2023-03-07 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skmsapp', '0019_post_author_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asset',
            old_name='assetid',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='asset',
            old_name='assetname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='countermeasure',
            old_name='countermeasureid',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='countermeasure',
            old_name='countermeasurename',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='countermeasuredescription',
            old_name='countermeasuredescription',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='threat',
            old_name='threatid',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='threat',
            old_name='threatname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='threatdescription',
            old_name='threatdescription',
            new_name='description',
        ),
    ]
