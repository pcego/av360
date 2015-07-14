from django.shortcuts import render
from ava360.models import Questionario, Avaliacao, Questao, Resposta
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ava360.forms import AvaliacaoForm, QuestionarioForm, QuestaoForm, RespostaForm


def responder_questao(request, pk_questao):
    dados = {}
    resposta = get_object_or_404(Resposta, questao = pk_questao)
    form = RespostaForm(request.POST or None, instance=resposta)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('url_responder', pk_questao)

    dados['form'] = form
    return render(request, 'ava360/resp_form_quest.html', dados)
    
def avaliacoes_list(request):
    ava = {}    
    ava['avaliacoes_list'] = Avaliacao.objects.filter(func_avaliador = request.user.id)    
    return render(request, 'ava360/avaliacoes_list.html', ava)

def responder_avaliacao(request, pk_questao):
    dados = {}        
    questao = get_object_or_404(Questao, pk=pk_questao)

    if request.method != 'POST':
        form = QuestaoForm(instance=questao)

        dados['form'] = form
        return render(request, 'ava360/resp_form_quest.html', dados)
    
    else:
        form = QuestaoForm(request.POST or None, instance=questao)
        if form.is_valid():
            form.save()
            return redirect('url_responder')
        else:
            dados['form'] = form
            return render(request, 'ava360/resp_form_quest.html', dados)


def responder(request, pk_questionario):
    dados = {}        
    dados['questoes'] = Questao.objects.filter(questionario = pk_questionario)
    return render(request, 'ava360/resp_avaliacao.html', dados)