# Create your views here.
from hotseat.models import Terminal

from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.utils import simplejson as json

from django.views.generic import YearArchiveView, MonthArchiveView,     \
                                    WeekArchiveView, DayArchiveView,    \
                                    ListView

from hotseat.models import Assignment, Terminal

def select_terminal(request):
    return render(request, 'helloworld.html')

def assign_terminal(request):
    return HttpResponse("Hello world. You're at the select terminal.")

def edit_terminal(request):
    return HttpResponse("Hello world. You're at the select terminal.")

def generate_report(request):
    return HttpResponse("Hello world. You're at the select terminal.")

class AssignmentViewMixin(object):
    model = Assignment
    date_field = 'created'
    context_object_name = 'assignment_list'
    paginate_by = 10
    def get_template_names(self):
        return 'manager/base_reports.html'

class AssignmentListView(AssignmentViewMixin, ListView):
    pass

class AssignmentYearView(AssignmentViewMixin, YearArchiveView):
    pass

class AssignmentMonthView(AssignmentViewMixin, MonthArchiveView):
    pass

class AssignmentWeekView(AssignmentViewMixin, WeekArchiveView):
    pass

class AssignmentDayView(AssignmentViewMixin, DayArchiveView):
    pass
