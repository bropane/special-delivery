# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-07 17:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0006_auto_20161007_1741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='device_id',
            new_name='device',
        ),
    ]
