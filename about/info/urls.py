#-*- coding:utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from info.views import person, person_edit

urlpatterns = patterns('',
    url(r'^$', person),
    url(r'^edit/$', person_edit),

    # Examples:
    # url(r'^$', 'about.views.home', name='home'),
    # url(r'^about/', include('about.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

)
