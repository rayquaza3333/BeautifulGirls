from django.shortcuts import render
from . import forms
import os
# Create your views here.

def index(request):
    return render(request,os.path.join('app_1','index.html'))

def form_name_view(request):

    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

    if form.is_valid():
        print('VALIDATION SUCCESS!')
        print('Name: '+form.cleaned_data['name'])
        print('Email: '+form.cleaned_data['email'])
        print('Text: '+form.cleaned_data['text'])

    return render(request,os.path.join('app_1','form_page.html'), {'form': form})

#Users view

def form_users_view(request):

    user = forms.Users()

    if request.method == 'POST':
        user = forms.Users(request.POST)

    if user.is_valid():
        user.save()

    return render(request,os.path.join('app_1','users.html'), {'user' : user })
