# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava360', '0012_resposta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questao',
            name='alternativa',
            field=models.ManyToManyField(related_name='alternativa_questao', to='ava360.Alternativa'),
        ),
        migrations.AlterField(
            model_name='questao',
            name='questionario',
            field=models.ManyToManyField(related_name='questionario_questao', to='ava360.Questionario'),
        ),
    ]
