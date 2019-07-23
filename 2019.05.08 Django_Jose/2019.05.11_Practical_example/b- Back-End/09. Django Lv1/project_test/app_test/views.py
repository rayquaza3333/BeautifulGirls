from django.shortcuts import render
from django.http import HttpResponse
import os
# Create your views here.
def index(request):
    return HttpResponse('<b> This is the original view without any template or static from index in app_test <b>')

def template(request):
    my_dict = {
        'insert_me1':'This is the first string',
        'insert_me2' :' And this is the second string'
    }
    return render(request,'index.html',context=my_dict)
