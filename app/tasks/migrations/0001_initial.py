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
                ('task_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField(max_length=2000)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_from', models.DateTimeField()),
                ('date_to', models.DateTimeField()),
                ('repeat', models.PositiveSmallIntegerField(choices=[(0, 'Do not repeat'), (1, 'Daily'), (2, 'Weekly'), (4, 'Monthly'), (8, 'Other (enter days count)')])),
                ('repeat_days', models.PositiveSmallIntegerField(default=0)),
                ('lat', models.DecimalField(null=True, max_digits=8, decimal_places=6, blank=True)),
                ('lng', models.DecimalField(null=True, max_digits=8, decimal_places=6, blank=True)),
                ('place_desc', models.CharField(max_length=250, blank=True)),
                ('public', models.BooleanField(default=False)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Deleted'), (1, 'Active'), (2, 'Done')], default=1)),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TaskFile',
            fields=[
                ('task_file_id', models.AutoField(serialize=False, primary_key=True)),
                ('file', models.FileField(upload_to='')),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'Unknown'), (1, 'Image'), (2, 'Audio'), (3, 'Video')], default=0)),
                ('size', models.IntegerField()),
                ('name', models.CharField(max_length=60, blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('task_id', models.ForeignKey(to='tasks.Task')),
            ],
        ),
        migrations.CreateModel(
            name='TaskLog',
            fields=[
                ('task_log_id', models.AutoField(serialize=False, primary_key=True)),
                ('description', models.TextField(max_length=1000)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(choices=[(False, 'Deleted'), (True, 'Active')], default=True)),
                ('task_id', models.ForeignKey(to='tasks.Task')),
            ],
        ),
    ]
