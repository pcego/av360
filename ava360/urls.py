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
]