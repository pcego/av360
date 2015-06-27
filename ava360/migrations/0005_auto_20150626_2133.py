# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava360', '0004_auto_20150626_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionario',
            name='ponto_forte',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='ponto_melhorar',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
    ]
