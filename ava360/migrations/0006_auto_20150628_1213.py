# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava360', '0005_auto_20150626_2133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('data_avaliacao', models.DateField()),
                ('ponto_forte', models.TextField(null=True, max_length=500, blank=True)),
                ('ponto_melhorar', models.TextField(null=True, max_length=500, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Avaliações',
                'verbose_name': 'Avaliação',
            },
        ),
        migrations.AlterModelOptions(
            name='funcionario',
            options={'verbose_name': 'Funcionário'},
        ),
        migrations.AlterModelOptions(
            name='questao',
            options={'verbose_name_plural': 'Questões', 'verbose_name': 'Questão'},
        ),
        migrations.AlterModelOptions(
            name='questionario',
            options={'verbose_name': 'Questionário'},
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='ponto_forte',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='ponto_melhorar',
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='func_avaliado',
            field=models.ForeignKey(to='ava360.Funcionario'),
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='questionario',
            field=models.ForeignKey(to='ava360.Questionario'),
        ),
    ]
