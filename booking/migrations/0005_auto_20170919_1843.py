# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20170919_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='concert',
            name='concert_end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='concert',
            name='concert_start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
