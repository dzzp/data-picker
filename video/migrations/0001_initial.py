# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-03 18:57
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import video.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('case_title', models.CharField(max_length=50)),
                ('case_path', models.FilePathField(blank=True)),
                ('group_hash_id', models.CharField(default=video.models._generateHash, max_length=8, unique=True)),
                ('generated_datetime', models.DateTimeField()),
                ('memo', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoadList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=7), size=None)),
                ('current', models.CharField(max_length=7)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.Case')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('hash_value', models.CharField(default=video.models._generateHash, max_length=7, unique=True)),
                ('person_path', models.FilePathField()),
                ('score', models.FloatField()),
                ('frame_num', models.IntegerField()),
                ('shot_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ProbeList',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.Case')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.Person')),
            ],
        ),
        migrations.CreateModel(
            name='TestVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='assets/')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('hash_value', models.CharField(default=video.models._generateHash, max_length=7, unique=True)),
                ('video_path', models.FilePathField()),
                ('date', models.DateField(default='0001-01-01')),
                ('time', models.TimeField(default='00:00:00')),
                ('memo', models.TextField(blank=True)),
                ('lat', models.FloatField(default=0.0)),
                ('lng', models.FloatField(default=0.0)),
                ('total_frame', models.IntegerField(default=0)),
                ('frame_rate', models.IntegerField(default=0)),
                ('is_detect_done', models.BooleanField(default=False)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.Case')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.Video'),
        ),
    ]
