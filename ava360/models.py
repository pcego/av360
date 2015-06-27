from django.db import models
from django.contrib.auth.models import User


class Cargo(models.Model):
	
	descricao= models.CharField(max_length=50)
	ativo = models.BooleanField(default=True)

	def __str__(self):
		return self.descricao

	
class Departamento(models.Model):
	
	descricao = models.CharField(max_length=100)
	ramal = models.CharField(max_length=5)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.descricao


class Funcionario(models.Model):
	
	usuario = models.OneToOneField(User)
	nome = models.CharField(max_length=100, blank=False)
	telefone = models.CharField(max_length=15, blank=False)
	departamento = models.ForeignKey(Departamento)
	ativo = models.BooleanField(default=True)
	resp = models.ForeignKey( 'self', null=True, blank=True, help_text='Responsável Pela Avaliação', related_name='responsavel' )
	cargo = models.ForeignKey(Cargo)	

	def __str__(self):
		return self.nome

class Questionario(models.Model):
	
	titulo = models.CharField(max_length=40)	
	data_criacao = models.DateField(blank=False)
	ponto_forte = models.TextField(max_length=500, null=True, blank=True)
	ponto_melhorar = models.TextField(max_length=500, null=True, blank=True)
	funcionario = models.ManyToManyField(Funcionario, related_name='Avaliado')	

	def __str__(self):
		return self.titulo


class Alternativa(models.Model):
	
	texto = models.CharField(max_length=100)

	def __str__(self):
		return self.texto


class Questao(models.Model):
	texto = models.CharField(max_length=500)
	questionario = models.ManyToManyField(Questionario)
	alternativa = models.ManyToManyField(Alternativa)	

	def __str__(self):
		return self.texto

	class Meta:
		verbose_name_plural = 'Questões'