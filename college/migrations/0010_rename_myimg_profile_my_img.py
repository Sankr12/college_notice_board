# Generated by Django 4.2.6 on 2023-11-27 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0009_profile_myimg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='myimg',
            new_name='my_img',
        ),
    ]
