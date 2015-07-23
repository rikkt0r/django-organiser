# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.PositiveSmallIntegerField(choices=[(0, 'No rush'), (1, 'Normal'), (2, 'Important')], default=1),
        ),
    ]
