# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-07 15:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0072_merge_20171105_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingoffer',
            name='artist_manager',
        ),
        migrations.RemoveField(
            model_name='concert',
            name='artist_manager',
        ),
    ]