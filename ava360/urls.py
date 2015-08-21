from django.conf.urls import include, url


urlpatterns = [
        
    url(r'^avaliaçoes_pendentes/$',
        'ava360.views.avaliacoes_list', 
        name='url_avaliacoes_pendentes'),

    url(r'^resposta/(?P<pk_avaliacao>\d+)/$',
        'ava360.views.responder',
        name='url_responder'),

     url(r'^questao_resp/(?P<pk_questao>\d+)/$',
        'ava360.views.responder_questao',
        name='url_questao_resp'),

     url(r'^relatorio/$',
        'ava360.views.relatorios',
        name='url_relatorios'),
]