# Generated by Django 4.2.6 on 2023-11-28 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0014_alter_question_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='cr_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
