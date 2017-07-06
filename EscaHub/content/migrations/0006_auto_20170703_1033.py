# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-03 05:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_remove_category_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itineraryday',
            name='trip',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='category',
        ),
        migrations.AddField(
            model_name='itineraryday',
            name='tripItinerary',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.TripItinerary'),
        ),
        migrations.AddField(
            model_name='trip',
            name='arrival_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='costing_excludes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='costing_includes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='departure_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='tripitinerary',
            name='day',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='tripitinerary',
            unique_together=set([('trip', 'day')]),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
