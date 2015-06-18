"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin, auth

urlpatterns = [

	url(r'^$', 'django.contrib.auth.views.login',
            {'template_name': 'index.html'}, name='url_login'),

    	url(r'^register$', 'project.views.register', name='register'),
    
    	url(r'^accounts/profile/$', 'project.views.dashboard',
    	name='url_dashborard'),

    	url(r'^logout/$', 'django.contrib.auth.views.logout',
        	{'template_name': 'registration/logout.html'}, name='url_logout'),

    	url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        	{'template_name': 'index.html'}, name='url_login'),

    	# Change Password URLs:
    	url(r'^accounts/password_change/$', 
        	'django.contrib.auth.views.password_change', 
        	{'post_change_redirect' : '/accounts/password_change/done/',
        	'template_name':'registration/password_change_form.html'}, 
        	name="password_change"), 
    
    	url(r'^accounts/password_change/done/$', 
        	'django.contrib.auth.views.password_change_done'),

    	#URL reset
    	url(r'^reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        	'project.views.reset_confirm', name='reset_confirm'),
    	url(r'^reset/$', 'project.views.reset', name='reset'),
    	url(r'^reset_succeful/$', 'project.views.password_confirmation', name='url_reset_suceful'),

    	url(r'^admin/', include(admin.site.urls)),   
]
