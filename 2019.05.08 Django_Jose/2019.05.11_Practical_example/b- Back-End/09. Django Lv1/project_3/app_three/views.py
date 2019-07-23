from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.

def index(request):
    return HttpResponse('<i> You are in the Home page')

def help(request):
    my_dict={
    'var1' : "<b> ok bro <b>",
    'var2' : '<i> and this is the second template tag'
    }
    return render(request,os.path.join('app_three','help.html'),context=my_dict)
