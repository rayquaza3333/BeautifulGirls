from django.shortcuts import render
from django.http import HttpResponse
import os
from app_4.models import Topic, Webpage, AccessReCord, Users
# Create your views here.

def index(request):
    return HttpResponse('<b>Ok man, this is from the first index<b>')

def complex(request):

    webpages_list = AccessReCord.objects
    date_dict= { 'access_records': webpages_list}

    my_dict= {
        'insert_me1':'OK this is a string',
        'insert_me2':'And this is another string'
    }

    return render(request,os.path.join('app_4','index.html'),context=date_dict)
