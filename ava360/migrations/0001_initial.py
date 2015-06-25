# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alternativa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('ramal', models.CharField(max_length=5)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=15)),
                ('ativo', models.BooleanField(default=True)),
                ('cargo', models.ForeignKey(to='ava360.Cargo')),
                ('departamento', models.ForeignKey(to='ava360.Departamento')),
                ('resp', models.ForeignKey(blank=True, to='ava360.Funcionario', related_name='responsavel', help_text='Responsável Pela Avalição', null=True)),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pontuacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('pontuacao', models.IntegerField()),
                ('func_test', models.ManyToManyField(to='ava360.Funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=500)),
                ('valor', models.IntegerField()),
                ('alternativa', models.ManyToManyField(to='ava360.Alternativa')),
                ('correta', models.ForeignKey(to='ava360.Alternativa', related_name='Resposta')),
            ],
        ),
        migrations.CreateModel(
            name='Questionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('nota', models.IntegerField(null=True)),
                ('data_criacao', models.DateField()),
                ('funcionario', models.ManyToManyField(to='ava360.Funcionario', related_name='Avaliado')),
            ],
        ),
        migrations.AddField(
            model_name='questao',
            name='questionario',
            field=models.ForeignKey(to='ava360.Questionario'),
        ),
        migrations.AddField(
            model_name='pontuacao',
            name='questao',
            field=models.ManyToManyField(to='ava360.Questao'),
        ),
    ]
