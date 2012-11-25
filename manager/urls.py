from django.conf.urls import patterns, url
from .views import select_terminal, assign_terminal, edit_terminal, generate_report

from manager import views

urlpatterns = patterns('', 
    url(r'^select_terminal/', select_terminal, name='selectTerminal'),
    url(r'^assign_terminal/', assign_terminal, name='assignTerminal'),
	url(r'^edit_terminal/', edit_terminal, name='editTerminal'),
	url(r'^generate_report/', generate_report, name='genrateReport')
	
)