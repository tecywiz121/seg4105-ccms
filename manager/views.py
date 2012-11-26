# Create your views here.
from hotseat.models import Terminal

from decimal import Decimal

from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.utils import simplejson as json

from django.views.generic import YearArchiveView, MonthArchiveView,     \
                                    WeekArchiveView, DayArchiveView,    \
                                    ListView

from hotseat.models import Assignment, Terminal
from .forms import ReportForm
from django.core.urlresolvers import reverse
import datetime

def select_terminal(request):
    context_all_terminals = Terminal.objects.all()
    #output = ""
    #for t in all_terminals_list:
	#    output += str(t.is_available) + " " + str(t.name) + " "
    #return HttpResponse(output)
	# output = ', '.join([str(t.is_available) for t in all_terminals_list])
    #return HttpResponse(output)
    return render(request, 'manager/selectTerminal.html', {'terminals':context_all_terminals})

def assign_terminal(request, terminal):
    terminalObj = get_object_or_404(Terminal, pk=terminal)
    return render(request, 'manager/assignTerminal.html', {'terminal':terminalObj.pk})

RATES_DICT = {"base":2.0, "promotion":1.50, "happyHour":1.0, "free":0.0}

@require_POST
def set_terminal(request, terminal):
    terminal = get_object_or_404(Terminal, pk=terminal)
    
    hours = float(request.POST["hours"])   
    minutes = float(request.POST["minutes"])
    rate = request.POST["rate"]
    discountType = request.POST["discount"]
       
    time = hours * 3600.0 + minutes * 60.0
    cost = RATES_DICT[rate] * (time/3600.0)
    
    print discountType
    if discountType == "flatamount":
        discountAmount = float(request.POST["amount"])
        cost -= discountAmount
    elif discountType == "percentage":
        discountPercent = float(request.POST["percent"])
        cost *= 1.0 - discountPercent/100.0
    
    if terminal.is_available:
        assignment = terminal.assign()
     
    else:
        assignment = terminal.current_assignment
    
    assignment.edit_time_remaining(time)
    assignment.edit_cost(cost)
    
    assignment.save()
        
    return redirect(select_terminal)
    
def generate_report(request):
    return HttpResponse("Hello world. You're at the select terminal.")

class AssignmentViewMixin(object):
    model = Assignment
    date_field = 'created'
    context_object_name = 'assignment_list'
    paginate_by = 10
    def get_template_names(self):
        return 'manager/base_reports.html'

    def post(self, *args, **kwargs):
        form = ReportForm(self.request.POST)
        if not form.is_valid():
            return self.get(*args, **kwargs)

        period = int(form.cleaned_data['period'])
        month = form.cleaned_data['month']
        year = int(form.cleaned_data['year'])
        day = int(form.cleaned_data['day'])
        date = datetime.datetime.strptime('{} {} {}'.format(year, month, day), '%Y %b %d')

        if period == ReportForm.MONTH:
            url = reverse('reportMonth', kwargs={'month': month, 'year': year})
        elif period == ReportForm.DAY:
            url = reverse('reportDay', kwargs={'month': month, 'year': year, 'day': day})
        elif period == ReportForm.WEEK:
            week = date.isocalendar()[1] + 1 # No idea why we need the +1
            url = reverse('reportWeek', kwargs={'year': year, 'week': week})
        return redirect(url)

class AssignmentListView(AssignmentViewMixin, ListView):
    pass

class AssignmentYearView(AssignmentViewMixin, YearArchiveView):
    pass

class AssignmentMonthView(AssignmentViewMixin, MonthArchiveView):
    default_period = ReportForm.MONTH

class AssignmentWeekView(AssignmentViewMixin, WeekArchiveView):
    default_period = ReportForm.WEEK

class AssignmentDayView(AssignmentViewMixin, DayArchiveView):
    default_period = ReportForm.DAY


def get_context_data(self, *args, **kwargs):
    # Call the base implementation first to get a context
    context = super(self.__class__, self).get_context_data(*args, **kwargs)
    # Add in a RequestForm
    if self.request.method == "POST":
        context['form'] = ReportForm(self.request.POST)
    else:
        context['form'] = ReportForm(initial={'period': getattr(self, 'default_period', ReportForm.DAY)})

    return context

AssignmentListView.get_context_data = get_context_data
AssignmentYearView.get_context_data = get_context_data
AssignmentMonthView.get_context_data = get_context_data
AssignmentDayView.get_context_data = get_context_data
AssignmentWeekView.get_context_data = get_context_data
