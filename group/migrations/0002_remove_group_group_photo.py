# Generated by Django 3.0.8 on 2020-10-05 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='group_photo',
        ),
    ]
