# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava360', '0015_avaliacao_titulo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questao',
            name='questionario',
        ),
        migrations.AddField(
            model_name='questionario',
            name='questao',
            field=models.ManyToManyField(to='ava360.Questao', related_name='questionario_questao'),
        ),
    ]
