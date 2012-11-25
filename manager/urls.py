from django.conf.urls import patterns, url
from .views import select_terminal, assign_terminal,    \
                    set_terminal,                      \
                    AssignmentYearView,                 \
                    AssignmentMonthView,                \
                    AssignmentDayView,                  \
                    AssignmentWeekView,                 \
                    AssignmentListView


from manager import views

urlpatterns = patterns('',
    url(r'^select_terminal/', select_terminal, name='selectTerminal'),
    url(r'^assign_terminal/(?P<terminal>[^/]*)/$', assign_terminal, name='assignTerminal'),
    url(r'^set_terminal/', set_terminal, name='setTerminal'),

    url(r'^assignments/$', AssignmentListView.as_view(), name='report'),
    url(r'^assignments/(?P<year>[0-9]+)/$', AssignmentYearView.as_view(), name='reportYear'),
    url(r'^assignments/(?P<year>[0-9]+)/(?P<month>[a-zA-Z]+)/$', AssignmentMonthView.as_view(), name='reportMonth'),
    url(r'^assignments/(?P<year>[0-9]+)/week/(?P<week>[0-9]+)/$', AssignmentWeekView.as_view(), name='reportWeek'),
    url(r'^assignments/(?P<year>[0-9]+)/(?P<month>[a-zA-Z]+)/(?P<day>[0-9]+)/$', AssignmentDayView.as_view(), name='reportDay'),
)
