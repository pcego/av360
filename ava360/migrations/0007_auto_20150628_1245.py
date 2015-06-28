# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava360', '0006_auto_20150628_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliacao',
            name='ponto_forte',
        ),
        migrations.RemoveField(
            model_name='avaliacao',
            name='ponto_melhorar',
        ),
        migrations.AddField(
            model_name='questionario',
            name='ponto_forte',
            field=models.TextField(null=True, max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='questionario',
            name='ponto_melhorar',
            field=models.TextField(null=True, max_length=500, blank=True),
        ),
    ]
