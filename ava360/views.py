from django.shortcuts import render
from ava360.models import Departamento
from django.shortcuts import render, redirect, get_object_or_404
from ava360.forms import DepartamentForm, Questionario, Avaliacao
from django.contrib.auth.decorators import login_required
from ava360.forms import AvaliacaoForm, QuestionarioForm

def departament_list(request):
    data = {}
    data['departament_list'] = Departamento.objects.all()
    return render(request, 'ava360/departament_list.html', data)


def departament_create(request, template_name='ava360/departament_form.html'):
    form = DepartamentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_avaliacoes_departament')
    return render(request, template_name, {'form':form})

@login_required
def departament_update(request, pk, template_name='ava360/departament_form.html'):
    departament = get_object_or_404(Departamento, pk=pk)
    form = DepartamentForm(request.POST or None, instance=departament)
    if form.is_valid():
        form.save()
        return redirect('url_avaliacoes_departament')
    return render(request, template_name, {'form':form, 'departament':departament})


def departament_delete(request, pk, template_name='ava360/confirm_delete.html'):
    departament = get_object_or_404(Departament, pk=pk)    
    if request.method=='POST':
        departament.delete()
        return redirect('url_avaliacoes_departament')
    return render(request, template_name, {'object':departament})


def questionario_form(request, pk):
    dados = {}
    questionario = get_object_or_404(Questionario, pk=pk)    
    form = QuestionarioForm(instance=questionario)
    dados['form'] = form
    return render(request, 'ava360/questionario_form.html', dados)
    
def avaliacoes_list(request):
    ava = {}    
    ava['avaliacoes_list'] = Avaliacao.objects.filter(func_avaliador = request.user.id)
    #ava['avaliacoes_list'] = Avaliacao.objects.all()
    return render(request, 'ava360/avaliacoes_list.html', ava)