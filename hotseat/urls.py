from django.conf.urls import patterns, include, url
from .views import login, logout, keepalive

urlpatterns = patterns('',
    url(r'^login/', login, name='hs_login'),
    url(r'^logout/', logout, name='hs_logout'),
    url(r'^keepalive/', keepalive, name='hs_keepalive'),
    # Examples:
    # url(r'^$', 'ccms.views.home', name='home'),
    # url(r'^ccms/', include('ccms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
