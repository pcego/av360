from django.forms import ModelForm
from ava360.models import Departament


class DepartamentForm(ModelForm):
	class Meta:
		model = Departament
		fields = ['description', 'phone']