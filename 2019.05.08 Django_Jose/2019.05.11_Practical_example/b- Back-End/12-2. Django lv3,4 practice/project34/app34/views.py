from django.shortcuts import render
from django.http import HttpResponse
from . import forms
import os
# Create your views here.

def index(request):
    return HttpResponse('<i> Hello </i>')



def form_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

    if form.is_valid():
        print('VALIDATION COMPLETE!')
        print(f"NAME: {form.cleaned_data['name']}")
        print(f"EMAIL: {form.cleaned_data['email']}")
        print(f"TEXT: {form.cleaned_data['text']}")

    return render(request,os.path.join('app34','formpage.html'),{'form':form})

def users_input_view(request):
    user = forms.UserForm()

    if request.method =='POST':
        user = forms.UserForm(request.POST)

    if user.is_valid():
        user.save()
    return render(request, os.path.join('app34','formpage.html'),{'form':user,'insert':'This works ok'})
