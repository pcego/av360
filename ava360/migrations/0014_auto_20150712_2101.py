# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava360', '0013_auto_20150712_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionario',
            name='ponto_forte',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='ponto_melhorar',
        ),
    ]
