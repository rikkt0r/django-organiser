# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organiser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskfile',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default='2015-06-28'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taskfile',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tasklog',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
