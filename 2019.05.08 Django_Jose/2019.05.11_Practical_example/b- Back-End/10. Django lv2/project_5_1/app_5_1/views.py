from django.shortcuts import render
from django.http import HttpResponse
from app_5_1.models import AccessRecord
import os
# Create your views here.

def index(request):
    return HttpResponse('<b> This is the default view</b>')

def access(request):

    access_list = AccessRecord.objects.all()
    my_dict = {'access_list' : access_list,'insert_me':'Be carefull, we watch every single move you made!'}

    return render(request,os.path.join('app_5_1','index.html'),context = my_dict)
