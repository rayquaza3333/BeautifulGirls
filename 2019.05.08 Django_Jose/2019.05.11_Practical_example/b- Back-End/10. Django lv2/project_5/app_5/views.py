from django.shortcuts import render
from django.http import HttpResponse
import os
from app_5.models import AccessRecord
# Create your views here.

def index(request):
    return HttpResponse('<b> Ok This is the first view </b>')

def app_5(request):
    return HttpResponse('<em> This is the HTTP code from a extension</em>')

def template(request):
    my_dict= {'insert_me':'This is injected into the template from render()'}
    return render(request,os.path.join('app_5','index.html'),context = my_dict)

def access(request):

    access_list = AccessRecord.objects.all()
    my_dict = {'access_list':access_list}

    return render(request,os.path.join('app_5','index.html'),context= my_dict)
