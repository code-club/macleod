from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import sujets.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'macleod.views.home', name='home'),
    # url(r'^macleod/', include('macleod.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url('^', include(sujets.urls))
)

urlpatterns += staticfiles_urlpatterns()
