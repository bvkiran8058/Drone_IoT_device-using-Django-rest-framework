# Generated by Django 5.0.6 on 2024-10-06 14:18

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drones', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='pilot',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='competition',
            name='drone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competitions', to='drones.drone'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='pilot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competitions', to='drones.pilot'),
        ),
        migrations.AlterField(
            model_name='drone',
            name='drone_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drone_cat', to='drones.dronecategory'),
        ),
        migrations.AlterField(
            model_name='drone',
            name='manfacturing_date',
            field=models.DateField(default=datetime.datetime(2024, 10, 6, 19, 48, 7, 959584)),
        ),
    ]
