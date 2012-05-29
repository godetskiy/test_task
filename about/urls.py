from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('about.info.urls')),
    #url(r'^accounts/login/$',  login),
    url(r'^accounts/login/$', login, {'template_name': 'registration/login.html'}),
    # Examples:
    # url(r'^$', 'about.views.home', name='home'),
    # url(r'^about/', include('about.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

)
