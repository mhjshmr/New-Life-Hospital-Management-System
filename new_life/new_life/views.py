from django.shortcuts import render
from django.http import request, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from . forms import LoginForm
from django.contrib.auth.views import LoginView
from django.views.defaults import page_not_found, server_error

def home(request):
    return render(request, 'index.html', {'name': 'Nihaal'})

def theme(request):
    print('exec')
    if 'is_dark_theme' in request.session:
        request.session['is_dark_theme'] = not request.session['is_dark_theme']
    else:
        request.session['is_dark_theme'] = True
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'), '/')

def about(request):
    return render(request, 'about.html')