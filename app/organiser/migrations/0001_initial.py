# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField(max_length=1000)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_from', models.DateTimeField()),
                ('date_to', models.DateTimeField()),
                ('amortisation', models.PositiveSmallIntegerField()),
                ('postpone_count', models.PositiveSmallIntegerField()),
                ('repeat', models.PositiveSmallIntegerField()),
                ('lat', models.DecimalField(decimal_places=6, max_digits=8)),
                ('lng', models.DecimalField(decimal_places=6, max_digits=8)),
                ('public', models.BooleanField(default=False)),
                ('status', models.PositiveSmallIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='TaskFile',
            fields=[
                ('task_file_id', models.AutoField(serialize=False, primary_key=True)),
                ('extension', models.CharField(max_length=4)),
                ('type', models.CharField(max_length=15)),
                ('size', models.IntegerField()),
                ('name', models.CharField(null=True, max_length=60)),
                ('file_location', models.CharField(max_length=120)),
                ('task_id', models.ForeignKey(to='organiser.Task')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=26)),
                ('email', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=32)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_logged', models.DateTimeField(blank=True, default=django.utils.datetime_safe.datetime.now)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='user_id',
            field=models.ForeignKey(to='organiser.User'),
        ),
    ]
