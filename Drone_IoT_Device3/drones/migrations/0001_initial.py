# Generated by Django 5.0.6 on 2024-10-06 12:35

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DroneCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('num_of_races', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Drone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('manfacturing_date', models.DateField(default=datetime.datetime(2024, 10, 6, 18, 5, 8, 635340))),
                ('participated_in_race_s', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('drone_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='done_cat', to='drones.dronecategory')),
            ],
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance_in_feet', models.FloatField(default=0)),
                ('date_of_competition', models.DateField()),
                ('drone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drones', to='drones.drone')),
                ('pilot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pilots', to='drones.pilot')),
            ],
        ),
    ]