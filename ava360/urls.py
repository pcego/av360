from django.conf.urls import include, url


urlpatterns = [
        
    url(r'^questionario/(?P<pk>\d+)$', 
        'ava360.views.questionario_form', 
        name='url_questionario'),   

    url(r'^avaliaçoes_pendentes/$',
        'ava360.views.avaliacoes_list', 
        name='url_avaliacoes_pendentes'),

    url(r'^resposta/(?P<pk_questionario>\d+)/$',
        'ava360.views.responder',
        name='url_responder'),

     url(r'^questao_resp/(?P<pk_questionario>\d+)/(?P<pk_questao>\d+)/$',
        'ava360.views.responder_avaliacao',
        name='url_questao_resp'),
]