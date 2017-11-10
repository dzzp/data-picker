# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 21:12
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_auto_20171109_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='case_title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='case',
            name='video_hash_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=7), blank=True, size=None),
        ),
    ]