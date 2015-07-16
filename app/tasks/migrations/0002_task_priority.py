# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.PositiveSmallIntegerField(choices=[(0, 'No rush'), (1, 'Just another task'), (2, 'Do it quickly'), (3, 'LIFE THREATENING')], default=1),
        ),
    ]
