# Create your views here.
from hotseat.models import Terminal

from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.utils import simplejson as json

def select_terminal(request):
    context_all_terminals = Terminal.objects.all()
    #output = ""
    #for t in all_terminals_list:
	#    output += str(t.is_available) + " " + str(t.name) + " "
    #return HttpResponse(output)
	# output = ', '.join([str(t.is_available) for t in all_terminals_list])
    #return HttpResponse(output)
    return render(request, 'managerTemplates\selectTerminal.html', {'terminals':context_all_terminals})

def assign_terminal(request):
    return HttpResponse("Hello world. You're at the select terminal.")

def edit_terminal(request):
    return HttpResponse("Hello world. You're at the select terminal.")

def generate_report(request):
    return HttpResponse("Hello world. You're at the select terminal.")




