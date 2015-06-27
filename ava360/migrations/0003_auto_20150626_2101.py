# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava360', '0002_auto_20150625_0006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pontuacao',
            name='func_test',
        ),
        migrations.RemoveField(
            model_name='pontuacao',
            name='questao',
        ),
        migrations.RemoveField(
            model_name='questao',
            name='correta',
        ),
        migrations.RemoveField(
            model_name='questao',
            name='valor',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='nota',
        ),
        migrations.AddField(
            model_name='cargo',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='questionario',
            name='ponto_forte',
            field=models.TextField(max_length=500, default='null'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionario',
            name='ponto_melhorar',
            field=models.TextField(max_length=500, default='1'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='resp',
            field=models.ForeignKey(help_text='Responsável Pela Avaliação', related_name='responsavel', null=True, to='ava360.Funcionario', blank=True),
        ),
        migrations.RemoveField(
            model_name='questao',
            name='questionario',
        ),
        migrations.AddField(
            model_name='questao',
            name='questionario',
            field=models.ManyToManyField(to='ava360.Questionario'),
        ),
        migrations.DeleteModel(
            name='Pontuacao',
        ),
    ]
