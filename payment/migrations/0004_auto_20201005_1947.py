# Generated by Django 3.0.8 on 2020-10-05 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0002_remove_group_group_photo'),
        ('payment', '0003_auto_20201005_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.Group'),
        ),
    ]