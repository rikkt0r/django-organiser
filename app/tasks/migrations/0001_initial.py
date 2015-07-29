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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField(max_length=2000)),
                ('priority', models.PositiveSmallIntegerField(default=1, choices=[(0, 'No rush'), (1, 'Normal'), (2, 'Important')])),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_from', models.DateTimeField()),
                ('date_to', models.DateTimeField()),
                ('repeat', models.PositiveSmallIntegerField(choices=[(0, 'Do not repeat'), (1, 'Daily'), (2, 'Weekly'), (4, 'Monthly'), (8, 'Other (enter days count)')])),
                ('repeat_days', models.PositiveSmallIntegerField(default=0)),
                ('lat', models.DecimalField(blank=True, decimal_places=6, null=True, max_digits=8)),
                ('lng', models.DecimalField(blank=True, decimal_places=6, null=True, max_digits=8)),
                ('place_desc', models.CharField(blank=True, max_length=250)),
                ('public', models.BooleanField(default=False)),
                ('status', models.PositiveSmallIntegerField(default=1, choices=[(0, 'Deleted'), (1, 'Active'), (2, 'Done')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TaskFile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('type', models.PositiveSmallIntegerField(default=0, choices=[(0, 'Unknown'), (1, 'Image'), (2, 'Audio'), (3, 'Video')])),
                ('size', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=60)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('task', models.ForeignKey(to='tasks.Task')),
            ],
        ),
        migrations.CreateModel(
            name='TaskLog',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.TextField(max_length=1000)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True, choices=[(False, 'Deleted'), (True, 'Active')])),
                ('task', models.ForeignKey(to='tasks.Task')),
            ],
        ),
    ]
