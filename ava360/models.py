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

	class Meta:
		verbose_name = 'Funcionário'

class Questionario(models.Model):
	
	titulo = models.CharField(max_length=40)	
	data_criacao = models.DateField(blank=False)	
	funcionario = models.ManyToManyField(Funcionario, related_name='Avaliado')
	
	def __str__(self):
		return self.titulo

	class Meta:
		verbose_name = 'Questionário'


class Alternativa(models.Model):
	
	texto = models.CharField(max_length=100)

	def __str__(self):
		return self.texto

class Questao(models.Model):
	texto = models.CharField(max_length=500)
	questionario = models.ManyToManyField(Questionario, related_name = 'questionario_questao')
	alternativa = models.ManyToManyField(Alternativa, related_name = 'alternativa_questao')	

	def __str__(self):
		return self.texto

	class Meta:
		verbose_name = 'Questão'
		verbose_name_plural = 'Questões'

class Avaliacao(models.Model):
	func_avaliado = models.ForeignKey(Funcionario)
	func_avaliador = models.ForeignKey(Funcionario, related_name = 'avaliador')
	questionario = models.ForeignKey(Questionario)
	data_avaliacao = models.DateField()	
	finalizada = models.BooleanField(default=False)	

	class Meta:
		verbose_name = 'Avaliação'
		verbose_name_plural = 'Avaliações'

class Resposta(models.Model):
	avaliacao = models.ForeignKey(Avaliacao)
	questao = models.ForeignKey(Questao)
	resposta = models.ForeignKey(Alternativa, blank=True, null=True)

	def __str__(self):
		return 'Status: ' + str(self.respondida)

		@property
		def respondida(self):
			return 'Aberta' if not self.resposta else 'Respondida'