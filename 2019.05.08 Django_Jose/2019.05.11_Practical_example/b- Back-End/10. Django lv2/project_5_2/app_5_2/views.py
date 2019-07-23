from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<b> This is the first view </b>')

def url(request):
    return HttpResponse('<em> This is run from urls.py in app_5_2</em>')

def access(request):
    pass
