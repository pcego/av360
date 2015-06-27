from django.forms import ModelForm
from ava360.models import Departamento, Questionario


class DepartamentForm(ModelForm):
	class Meta:
		model = Departamento
		fields = ['descricao', 'ramal', 'active']

class QuestionarioForm(ModelForm):
	class Meta:
		model = Questionario
		fields = ['titulo']