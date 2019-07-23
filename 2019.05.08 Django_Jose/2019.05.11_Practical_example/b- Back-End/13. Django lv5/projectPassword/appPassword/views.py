from django.shortcuts import render
from appPassword.forms import UserForm, UserProfileInfoForm

# Import more for creating login logout:

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'appPassword/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

@login_required # We are changing the user_login to login_required(user_login)
def user_logout(request):  #But actually, just remember this simple: We add a required status for login
    logout(request)
    return HttpResponseRedirect(reverse('index')) # (?)

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm( request.POST,request.FILES)
        profile_form = UserProfileInfoForm( request.POST,request.FILES)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password) # Firstly, because form doesn't have set_password method
            user.save() #Secondly, we can only interact with data in database through models

            profile = profile_form.save(commit = False)
            profile.user = user
            # profile.portfolio_site = request.FILES['profile_pic']
            # profile.portfolio_site ='http://okman.ok'  #<< This code's purpose is to test whether code block work or not

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']


            profile.save()

            registered = True


        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'appPassword/registration.html',
                                {'user_form': user_form,
                                'profile_form':profile_form,
                                'registered':registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('special'))

            else:
                return HttpResponse("ACCOUNT IS NOT ACTIVE")
        else:
            print("Someone tried to login and failed")
            print(f"Username: {username} and password: {password}")
            return HttpResponse("Invalid login detail supplied!")
    else:
        return render(request,'appPassword/login.html',{})
