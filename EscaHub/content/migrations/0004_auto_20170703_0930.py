# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-03 04:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20170703_0927'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ItineraryDays',
            new_name='ItineraryDay',
        ),
    ]
