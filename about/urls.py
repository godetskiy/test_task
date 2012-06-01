from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('about.info.urls')),
    url(r'^accounts/login/$', login, {'template_name': 'registration/login.html'}),
)
