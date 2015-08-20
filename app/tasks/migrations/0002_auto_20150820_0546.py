# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskfile',
            name='file',
            field=models.FileField(upload_to='documents/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='taskfile',
            name='status',
            field=models.BooleanField(default=True, choices=[(False, 'Deleted'), (True, 'Active')]),
        ),
    ]
