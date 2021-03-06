# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-03 03:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_tripitinerary'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItineraryDays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('slot1', models.CharField(blank=True, max_length=300, null=True)),
                ('slot2', models.CharField(blank=True, max_length=300, null=True)),
                ('slot3', models.CharField(blank=True, max_length=300, null=True)),
                ('slot4', models.CharField(blank=True, max_length=300, null=True)),
                ('slot5', models.CharField(blank=True, max_length=300, null=True)),
                ('slot6', models.CharField(blank=True, max_length=300, null=True)),
                ('slot7', models.CharField(blank=True, max_length=300, null=True)),
                ('slot8', models.CharField(blank=True, max_length=300, null=True)),
                ('slot9', models.CharField(blank=True, max_length=300, null=True)),
                ('slot10', models.CharField(blank=True, max_length=300, null=True)),
                ('slot11', models.CharField(blank=True, max_length=300, null=True)),
                ('slot12', models.CharField(blank=True, max_length=300, null=True)),
                ('slot13', models.CharField(blank=True, max_length=300, null=True)),
                ('slot14', models.CharField(blank=True, max_length=300, null=True)),
                ('slot15', models.CharField(blank=True, max_length=300, null=True)),
                ('slot16', models.CharField(blank=True, max_length=300, null=True)),
                ('slot17', models.CharField(blank=True, max_length=300, null=True)),
                ('slot18', models.CharField(blank=True, max_length=300, null=True)),
                ('slot20', models.CharField(blank=True, max_length=300, null=True)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Trip')),
            ],
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d1s1',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d1s10',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d1s11',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d1s12',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d1s13',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d1s14',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d1s15',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d1s16',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d1s2',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d1s3',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d1s4',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d1s5',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d1s6',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d1s7',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d1s8',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d1s9',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d2s1',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d2s10',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d2s11',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d2s12',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d2s13',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d2s14',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d2s15',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d2s16',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d2s2',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d2s3',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d2s4',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d2s5',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d2s6',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d2s7',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d2s8',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d2s9',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d3s1',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d3s10',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d3s11',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d3s12',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d3s13',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d3s14',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d3s15',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d3s16',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d3s2',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d3s3',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d3s4',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d3s5',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d3s6',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d3s7',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d3s8',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d3s9',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d4s1',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d4s10',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d4s11',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d4s12',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d4s13',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d4s14',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d4s15',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d4s16',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d4s2',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d4s3',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d4s4',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d4s5',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d4s6',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d4s7',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d4s8',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d4s9',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d5s1',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d5s10',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d5s11',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d5s12',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d5s13',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d5s14',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d5s15',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d5s16',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d5s2',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d5s3',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d5s4',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d5s5',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d5s6',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d5s7',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d5s8',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='d5s9',
        ),
        migrations.AddField(
            model_name='tripitinerary',
            name='day',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
