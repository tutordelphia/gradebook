# Generated by Django 2.0.2 on 2018-03-19 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0002_auto_20180319_0244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='include_students',
        ),
    ]