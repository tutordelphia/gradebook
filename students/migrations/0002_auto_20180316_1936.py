# Generated by Django 2.0.2 on 2018-03-16 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('assignments', models.ManyToManyField(to='assignments.Assignment')),
            ],
        ),
        migrations.DeleteModel(
            name='Students',
        ),
    ]
