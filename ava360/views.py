from django.shortcuts import render
from ava360.models import Questionario, Avaliacao, Questao, Resposta
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ava360.forms import AvaliacaoForm, QuestionarioForm, QuestaoForm, RespostaForm


def responder_questao(request, pk_questao):
    dados = {}
    resposta = get_object_or_404(Resposta, pk = pk_questao)
    form = RespostaForm(request.POST or None, instance=resposta)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return responder(request, resposta.avaliacao.id)
            
    dados['form'] = form
    return render(request, 'ava360/resp_form_quest.html', dados)
    
def avaliacoes_list(request):
    ava = {}    
    ava['avaliacoes_list'] = Resposta.objects.filter(
        avaliacao__func_avaliador = request.user.id, resposta__isnull=True).distinct('avaliacao')
    
    if ava['avaliacoes_list'].__len__() > 0:       
        return render(request, 'ava360/avaliacoes_list.html', ava)
    
    else:
        return render(request, 'ava360/aviso.html')

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


def responder(request, pk_avaliacao):
    dados = {}
    avaliacao = get_object_or_404(Avaliacao, pk=pk_avaliacao)
    resposta = Resposta.objects.filter(avaliacao__func_avaliador = request.user.id,
        avaliacao = avaliacao, resposta__isnull=True)
    
    if resposta:
        dados['form'] = RespostaForm(instance=avaliacao)
        dados['questoes'] = resposta
        return render(request, 'ava360/resp_avaliacao.html', dados)
    else:
        return redirect('url_avaliacoes_pendentes')
        
    