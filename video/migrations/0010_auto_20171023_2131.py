# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 21:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0009_person_hash_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
