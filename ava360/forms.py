from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from ava360.models import Departamento
from ava360.models import Questionario, Avaliacao, Questao, Alternativa, Resposta
from django import forms


class QuestionarioForm(ModelForm):
	class Meta:
		model = Questionario
		questao = forms.ModelMultipleChoiceField(queryset=Questao.objects.all())
		exclude = []

class AvaliacaoForm(ModelForm):
	class Meta:
		model = Avaliacao		
		exclude = []

class QuestaoForm(forms.ModelForm):
    alternativa = forms.ModelMultipleChoiceField(
        widget=forms.RadioSelect,
        queryset=[])

    class Meta:
        model = Questao
        fields = ('texto', 'alternativa',)


    def __init__(self, *args, **kwargs):
        super(QuestaoForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:            
            self.fields['alternativa'].queryset = Questao.objects.get(
                pk=self.instance.pk).alternativa.all()
            self.fields['texto'].widget.attrs['readonly'] = True

class RespostaForm(forms.ModelForm):
    class Meta:
        model = Resposta
        fields = ('avaliacao', 'questao','resposta')

    def __init__(self, *args, **kwargs):
        super(RespostaForm, self).__init__(*args, **kwargs)

        self.fields['respondida'].widget = forms.RadioSelect()
        self.fields['respondida'].empty_label=None

        self.fields['respondida'].queryset = Resposta.objects.get(
           pk=self.instance.pk).questao.alternativa.all()