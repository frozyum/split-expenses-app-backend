# Generated by Django 3.0.8 on 2020-10-03 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('person', '0014_auto_20201003_1524'),
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('date', models.DateTimeField()),
                ('currency', models.CharField(max_length=5)),
                ('froom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from+', to='person.Person')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.Group')),
                ('too', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to', to='person.Person')),
            ],
        ),
    ]