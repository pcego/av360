from django.contrib import admin
from ava360.models import Departamento, Alternativa
from ava360.models import Funcionario, Cargo, Questao, Questionario

class FuncionarioAdmin(admin.ModelAdmin):
	list_display = ('nome', 'telefone', 'departamento', 'cargo', 'resp', 'ativo')
	list_filter = ['id', 'nome', 'cargo', 'responsavel', 'departamento']
	search_fields = ['id', 'nome', 'cargo', 'responsavel', 'departamento']
	#actions = ['seta_cliente_inativo', 'seta_cliente_ativo']

class DepartamentoAdmin(admin.ModelAdmin):
	list_display = ('descricao', 'ramal', 'active')
	list_filter = ['id', 'descricao']
	search_fields = ['id', 'descricao']

class FuncionarioAdmin(admin.ModelAdmin):
	list_display = ('nome', 'telefone', 'departamento', 'cargo', 'resp', 'ativo')
	list_filter = ['id', 'nome', 'cargo', 'responsavel', 'departamento']
	search_fields = ['id', 'nome', 'cargo', 'responsavel', 'departamento']




admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Cargo)
admin.site.register(Questao)
admin.site.register(Questionario)
admin.site.register(Alternativa)