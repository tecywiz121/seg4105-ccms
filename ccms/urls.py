from django.conf.urls import patterns, include, url
import hotseat.urls
import manager.urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/', include(hotseat.urls)),
	url(r'^', include(manager.urls)),
    # Examples:
    # url(r'^$', 'ccms.views.home', name='home'),
    # url(r'^ccms/', include('ccms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
