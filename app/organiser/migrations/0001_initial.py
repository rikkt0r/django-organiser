# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField(max_length=2000)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_from', models.DateTimeField()),
                ('date_to', models.DateTimeField(blank=True, null=True)),
                ('repeat', models.PositiveSmallIntegerField(blank=True, default=0, choices=[(0, 'Do not repeat'), (1, 'Daily'), (2, 'Weekly'), (4, 'Monthly'), (8, 'Other (enter days count)')])),
                ('repeat_days', models.PositiveSmallIntegerField(blank=True, default=0)),
                ('lat', models.DecimalField(max_digits=8, blank=True, decimal_places=6, default=0.0)),
                ('lng', models.DecimalField(max_digits=8, blank=True, decimal_places=6, default=0.0)),
                ('place_desc', models.CharField(blank=True, max_length=80)),
                ('public', models.BooleanField(default=False)),
                ('status', models.PositiveSmallIntegerField(default=1)),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TaskFile',
            fields=[
                ('task_file_id', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='')),
                ('type', models.CharField(max_length=15)),
                ('size', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=60)),
                ('task_id', models.ForeignKey(to='organiser.Task')),
            ],
        ),
        migrations.CreateModel(
            name='TaskLog',
            fields=[
                ('task_log_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=1000)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('task_id', models.ForeignKey(to='organiser.Task')),
            ],
        ),
    ]
