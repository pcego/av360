from django.conf.urls import include, url


urlpatterns = [
    
    url(r'^departament/$',
        'ava360.views.departament_list', 
        name='url_avaliacoes_departament'),
    
    url(r'^new$',
        'ava360.views.departament_create',
        name='url_departament_new'),

    url(r'^edit/(?P<pk>\d+)$',
        'ava360.views.departament_update',
        name='url_departament_edit'),
    
    url(r'^delete/(?P<pk>\d+)$',
        'ava360.views.departament_delete',
        name='url_departament_delete'),
    
    url(r'^questionario/(?P<pk>\d+)$', 
        'ava360.views.questionario_form', 
        name='url_questionario'),   

    url(r'^avaliaçoes_pendentes/$',
        'ava360.views.avaliacoes_list', 
        name='url_avaliacoes_pendentes'),

     url(r'^questao_resp/(?P<pk_questionario>\d+)/(?P<pk_questao>\d+)/$',
        'ava360.views.responder_avaliacao',
        name='url_questao_resp'),

     url(r'^resposta/(?P<pk_questionario>\d+)/$',
        'ava360.views.responder',
        name='url_responder'),
]