# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava360', '0011_auto_20150702_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('avaliacao', models.ForeignKey(to='ava360.Avaliacao')),
                ('questao', models.ForeignKey(to='ava360.Questao')),
                ('resposta', models.ForeignKey(null=True, blank=True, to='ava360.Alternativa')),
            ],
        ),
    ]
