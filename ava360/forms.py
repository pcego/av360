from django.forms import ModelForm
from ava360.models import Departamento


class DepartamentForm(ModelForm):
	class Meta:
		model = Departamento
		fields = ['descricao', 'ramal']