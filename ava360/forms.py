from django.forms import ModelForm
from ava360.models import Departamento
from ava360.models import Questionario, Avaliacao


class DepartamentForm(ModelForm):
	class Meta:
		model = Departamento
		fields = ['descricao', 'ramal', 'active']

class QuestionarioForm(ModelForm):
	class Meta:
		model = Questionario
		exclude = []

class AvaliacaoForm(ModelForm):
	class Meta:
		model = Avaliacao
		exclude = []