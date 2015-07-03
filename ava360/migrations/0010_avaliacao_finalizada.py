# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava360', '0009_auto_20150628_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacao',
            name='finalizada',
            field=models.BooleanField(default='1'),
            preserve_default=False,
        ),
    ]
