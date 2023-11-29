# Generated by Django 4.2.6 on 2023-11-27 10:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0007_profile_pn_profile_rn_alter_profile_marks_aggr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pn',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True, validators=[django.core.validators.RegexValidator('^0?[5-9]{1}\\d{9}$')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='rn',
            field=models.IntegerField(blank=True, null=True, unique=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]