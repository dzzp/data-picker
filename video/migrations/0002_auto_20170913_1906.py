# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='running_time',
            field=models.TimeField(),
        ),
    ]