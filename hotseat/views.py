# Create your views here.
from .forms import LoginForm, LogoutForm, KeepaliveForm
from .models import Terminal

from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.utils import simplejson as json

@csrf_exempt
@require_POST
def login(request):
    """Accepts a password and returns a token to track time usage"""
    form = LoginForm(request.POST)
    if not form.is_valid():
        return HttpResponseBadRequest(json.dumps({'error': form.errors}), mimetype='application/json')

    password = form.cleaned_data['password']
    terminal_id = form.cleaned_data['terminalId']

    terminal = get_object_or_404(Terminal, pk=terminal_id)

    if not terminal.check_password(password):
        return HttpResponseForbidden('Incorrect Password')

    assignment = terminal.current_assignment
    assignment.generate_token()
    assignment.save()

    return HttpResponse(json.dumps({'token': assignment.keepalive_token,
                                    'time_remaining': assignment.time_remaining}), mimetype='application/json')


@csrf_exempt
@require_POST
def logout(request):
    form = LogoutForm(request.POST)
    if not form.is_valid():
        return HttpResponseBadRequest(form.errors)
    return HttpResponse('Success')

@csrf_exempt
@require_POST
def keepalive(request):
    form = KeepaliveForm(request.POST)
    if not form.is_valid():
        return HttpResponseBadRequest(form.errors)
    return HttpResponse('Success')
