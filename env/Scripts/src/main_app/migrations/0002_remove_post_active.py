# Generated by Django 3.0.6 on 2020-05-30 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='active',
        ),
    ]