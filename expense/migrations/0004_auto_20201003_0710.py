# Generated by Django 3.0.8 on 2020-10-03 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
        ('person', '0011_auto_20201002_1900'),
        ('expense', '0003_auto_20201002_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persons', to='person.Person'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.Group'),
        ),
    ]