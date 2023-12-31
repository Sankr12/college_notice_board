# Generated by Django 4.2.6 on 2023-11-27 08:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0006_profile_marks_10_profile_marks_12_profile_marks_aggr'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pn',
            field=models.IntegerField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator('^0?[5-9]{1}\\d{9}$')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='rn',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='marks_aggr',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(200)]),
        ),
    ]
