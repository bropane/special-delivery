# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-07 17:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0005_auto_20161006_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='device_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device_manager.Device'),
        ),
    ]
