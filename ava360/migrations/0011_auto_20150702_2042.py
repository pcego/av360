# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava360', '0010_avaliacao_finalizada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='finalizada',
            field=models.BooleanField(default=False),
        ),
    ]
