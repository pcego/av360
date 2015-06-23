from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm


urlpatterns = [

    url(r'^$', 'django.contrib.auth.views.login',
            {'template_name': 'index.html'}, name='url_login'),

    url(r'^avaliacoes/', include('ava360.urls')),

    url(r'^register/', CreateView.as_view(
            template_name='registration/register.html',
            form_class=UserCreationForm,
            success_url='/',
    ), name='register',),
    
    url(r'^accounts/', include('django.contrib.auth.urls')),

    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'registration/logout.html'}, name='url_logout'),

    url(r'^accounts/profile/$', 'project.views.dashboard',
    name='url_dashborard'),

    url(r'^change-password/$', 'django.contrib.auth.views.password_change', {
    'template_name': 'registration/password_change_form.html'}, name="password-change"),

    url(r'^change-password-done/$', 'django.contrib.auth.views.password_change_done', {
    'template_name': 'registration/password_change_done.html'
    }, name="password-change-done"),

    url(r'^admin/', include(admin.site.urls)),
]
