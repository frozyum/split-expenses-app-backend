# Generated by Django 3.0.8 on 2020-10-03 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
        ('person', '0014_auto_20201003_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.Group'),
        ),
    ]
