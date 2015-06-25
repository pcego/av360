# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ava360', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alternativa',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('texto', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('descricao', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=15)),
                ('ativo', models.BooleanField(default=True)),
                ('cargo', models.ForeignKey(to='ava360.Cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Pontuacao',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('descricao', models.CharField(max_length=100)),
                ('pontuacao', models.IntegerField()),
                ('func_test', models.ManyToManyField(to='ava360.Funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('texto', models.CharField(max_length=500)),
                ('valor', models.IntegerField()),
                ('alternativa', models.ManyToManyField(to='ava360.Alternativa')),
                ('correta', models.ForeignKey(related_name='Resposta', to='ava360.Alternativa')),
            ],
        ),
        migrations.CreateModel(
            name='Questionario',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('titulo', models.CharField(max_length=40)),
                ('nota', models.IntegerField(null=True)),
                ('data_criacao', models.DateField()),
                ('funcionario', models.ManyToManyField(related_name='Avaliado', to='ava360.Funcionario')),
            ],
        ),
        migrations.RenameModel(
            old_name='Departament',
            new_name='Departamento',
        ),
        migrations.RenameField(
            model_name='departamento',
            old_name='description',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='departamento',
            old_name='phone',
            new_name='ramal',
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
        migrations.AddField(
            model_name='funcionario',
            name='departamento',
            field=models.ForeignKey(to='ava360.Departamento'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='resp',
            field=models.ForeignKey(null=True, blank=True, to='ava360.Funcionario', related_name='responsavel', help_text='Responsável Pela Avalição'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='usuario',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
