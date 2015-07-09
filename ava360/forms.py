from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from ava360.models import Departamento
from ava360.models import Questionario, Avaliacao, Questao, Alternativa
from django import forms


class DepartamentForm(ModelForm):
	class Meta:
		model = Departamento
		fields = ['descricao', 'ramal', 'active']

class QuestionarioForm(ModelForm):
	class Meta:
		model = Questionario
		questao = forms.ModelMultipleChoiceField(queryset=Questao.objects.all())
		exclude = []

class AvaliacaoForm(ModelForm):
	class Meta:
		model = Avaliacao		
		exclude = []

