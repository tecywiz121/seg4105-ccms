# Create your views here.
from hotseat.models import Terminal

from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.utils import simplejson as json

def select_terminal(request):
    return render(request, 'helloworld.html')

def assign_terminal(request):
    return HttpResponse("Hello world. You're at the select terminal.")

def edit_terminal(request):
    return HttpResponse("Hello world. You're at the select terminal.")

def generate_report(request):
    return HttpResponse("Hello world. You're at the select terminal.")




