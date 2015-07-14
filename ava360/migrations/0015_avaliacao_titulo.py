# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava360', '0014_auto_20150712_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacao',
            name='titulo',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
    ]
