# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava360', '0008_avaliacao_func_avaliador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliacao',
            name='func_avaliador',
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='func_avaliador',
            field=models.ForeignKey(default='1', related_name='avaliador', to='ava360.Funcionario'),
            preserve_default=False,
        ),
    ]
