# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0005_auto_20171109_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
