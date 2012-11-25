from django.conf.urls import patterns, url
from .views import login, keepalive

urlpatterns = patterns('',
    url(r'^login/', login, name='hs_login'),
    url(r'^logout/', keepalive, name='hs_logout'),
    url(r'^keepalive/', keepalive, name='hs_keepalive'),
    # Examples:
    # url(r'^$', 'ccms.views.home', name='home'),
    # url(r'^ccms/', include('ccms.foo.urls')),
)
