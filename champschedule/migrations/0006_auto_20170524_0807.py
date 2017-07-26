# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-24 13:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('champschedule', '0005_authuser_driver_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['start']},
        ),
        migrations.AlterField(
            model_name='event',
            name='driver_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='champschedule.Driver'),
        ),
    ]