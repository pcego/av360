from django.contrib import admin
from ava360.models import Departamento, Alternativa
from ava360.models import Funcionario, Cargo, Questao, Questionario

admin.site.register(Departamento)
admin.site.register(Funcionario)
admin.site.register(Cargo)
admin.site.register(Questao)
admin.site.register(Questionario)
admin.site.register(Alternativa)