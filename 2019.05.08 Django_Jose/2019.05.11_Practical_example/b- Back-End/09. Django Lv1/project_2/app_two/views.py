from django.shortcuts import render
from django.http import HttpResponse
import os
# Create your views here.



def index(request):
    my_dict={'insert_me':"Hello, now I am from app_two/views.py"}
    return render(request,os.path.join('app_two','index.html'),context=my_dict)
