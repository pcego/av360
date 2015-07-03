from django.contrib import admin
from ava360.models import Departamento, Alternativa
from ava360.models import Funcionario, Cargo, Questao, Questionario, Avaliacao


class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'departamento', 'cargo', 'resp', 'ativo')
    list_filter = ['id', 'nome', 'cargo', 'responsavel', 'departamento']
    search_fields = ['id', 'nome', 'cargo', 'responsavel', 'departamento']
	#actions = ['seta_cliente_inativo', 'seta_cliente_ativo']

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'ramal', 'active')
    list_filter = ['id', 'descricao']
    search_fields = ['id', 'descricao']


class QuestaoAdminLine(admin.TabularInline):
    model = Questao.alternativa.through
    verbose_name_plural = 'Alternativas'
    verbose_name='Questões'


class QuestaoAdmin(admin.ModelAdmin):
    inlines = (QuestaoAdminLine, )
    exclude = ['alternativa']


class QuestionarioAdminLine(admin.TabularInline):
    model = Questao.questionario.through
    verbose_name_plural = 'Questões'


class QuestionarioAdmin(admin.ModelAdmin):	
    list_filter = ['titulo']
    search_fields = ['titulo', 'data_criacao']
    inlines = (QuestionarioAdminLine,)

class AvaliacaoAdmin(admin.ModelAdmin):   
    list_display = ('func_avaliado', 'func_avaliador', 'data_avaliacao')
    list_filter = ['func_avaliado', 'func_avaliador', 'data_avaliacao']
    verbose_name_plural = 'Avaliações'

admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Cargo)
admin.site.register(Questao, QuestaoAdmin)
admin.site.register(Questionario, QuestionarioAdmin)
admin.site.register(Alternativa)
admin.site.register(Avaliacao, AvaliacaoAdmin)
