# Generated by Django 4.2.6 on 2023-11-27 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0004_remove_profile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='sem',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], default=1),
        ),
    ]
