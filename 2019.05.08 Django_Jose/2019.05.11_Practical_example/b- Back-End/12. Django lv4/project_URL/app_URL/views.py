from django.shortcuts import render
import os

# Create your views here.

def index(request):
    return render(request, os.path.join('app_URL','index.html'))

def other(request):
    return render(request, os.path.join('app_URL','other.html'))


def relative(request):
    my_dict = { 'text':'Hello this is text variable','number': 100 }
    return render(request,os.path.join( 'app_URL','relative_url_template_tags.html'), context = my_dict)

def base(request):
    return render(request,os.path.join( 'app_URL','base.html'))
