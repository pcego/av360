from django.shortcuts import render
from ava360.models import Departamento
from django.shortcuts import render, redirect, get_object_or_404
from ava360.forms import DepartamentForm

@login_required
def departament_list(request):
    data = {}
    data['departament_list'] = Departamento.objects.all()
    return render(request, 'ava360/departament_list.html', data)

@login_required
def departament_create(request, template_name='ava360/departament_form.html'):
    form = DepartamentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_avaliacoes_departament')
    return render(request, template_name, {'form':form})

@login_required
def departament_update(request, pk, template_name='ava360/departament_form.html'):
    departament = get_object_or_404(Departament, pk=pk)
    form = DepartamentForm(request.POST or None, instance=departament)
    if form.is_valid():
        form.save()
        return redirect('url_avaliacoes_departament')
    return render(request, template_name, {'form':form, 'departament':departament})

@login_required
def departament_delete(request, pk, template_name='ava360/confirm_delete.html'):
    departament = get_object_or_404(Departament, pk=pk)    
    if request.method=='POST':
        departament.delete()
        return redirect('url_avaliacoes_departament')
    return render(request, template_name, {'object':departament})
