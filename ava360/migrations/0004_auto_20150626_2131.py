# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava360', '0003_auto_20150626_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionario',
            name='ponto_forte',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='ponto_melhorar',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
