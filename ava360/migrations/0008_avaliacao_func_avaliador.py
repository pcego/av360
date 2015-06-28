# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava360', '0007_auto_20150628_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacao',
            name='func_avaliador',
            field=models.ManyToManyField(related_name='avaliador', to='ava360.Funcionario'),
        ),
    ]
