from django.shortcuts import render
from ava360.models import Questionario, Avaliacao, Questao, Resposta
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ava360.forms import AvaliacaoForm, QuestionarioForm, QuestaoForm


def questionario_form(request, pk):
    data = {}
    data['respostas'] = Resposta.objects.filter(
        avaliacao__func_avaliador__user = request.user)
    
    return render(request, 'ava360/questionario_form.html', data)
    
def avaliacoes_list(request):
    ava = {}    
    ava['avaliacoes_list'] = Avaliacao.objects.filter(func_avaliador = request.user.id)    
    return render(request, 'ava360/avaliacoes_list.html', ava)

def responder_avaliacao(request, pk_questionario, pk_questao):
    dados = {}    
    questionario = get_object_or_404(Questionario, pk=pk_questionario)
    questao = get_object_or_404(Questao, pk=pk_questao)

    if request.method != 'POST':
        form = QuestaoForm(instance=questao)

        dados['form'] = form

        return render(request, 'ava360/resp_form_quest.html', dados)
    
    else:
        form = QuestaoForm(request.POST or None, instance=questao)
        if form.is_valid():
            form.save()
            return redirect('url_questao_resp')
        else:
            dados['form'] = form
            return render(request, 'ava360/resp_form_quest.html', dados)


def responder(request, pk_questionario):
    dados = {}        
    dados['questoes'] = Questao.objects.filter(questionario = pk_questionario)
    return render(request, 'ava360/resp_avaliacao.html', dados)