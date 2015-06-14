# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organiser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskfile',
            name='extension',
        ),
        migrations.RemoveField(
            model_name='taskfile',
            name='file_location',
        ),
        migrations.AddField(
            model_name='taskfile',
            name='file',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
