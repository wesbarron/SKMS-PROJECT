# Generated by Django 4.1.6 on 2023-03-06 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skmsapp', '0014_assets_countermeasures_threats_alter_post_comments_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Assets',
            new_name='Asset',
        ),
        migrations.RenameModel(
            old_name='Countermeasures',
            new_name='Countermeasure',
        ),
        migrations.RenameModel(
            old_name='CountermeasureDescriptions',
            new_name='CountermeasureDescription',
        ),
        migrations.RenameModel(
            old_name='Threats',
            new_name='Threat',
        ),
        migrations.RenameModel(
            old_name='ThreatDescriptions',
            new_name='ThreatDescription',
        ),
    ]
