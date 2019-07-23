from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm

# Importing for registration, login, logout
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

#index
def index(request):
    return render(request,'app/index.html')

#register
def register(request):

    #condition to decide whether send register form or thank for registration

    #Define the forms
    user_form = UserForm(request.POST, request.FILES)
    profile_form = UserProfileInfoForm(request.POST, request.FILES)

    if request.method == 'POST':
        if user_form.is_valid() and profile_form.is_valid():

            #save user basic info to database and hash password
            user = user_form.save()
            user.set_password()
            user.save()

            # Save profile to database
            profile = profile_form.save(commit = False) # commit = False so that data can be adjust, at this case
            profile.user = user                         # I think that's profile.user
            profile.save()

            return HttpResponse('Thank you for registering')
        else:
            # IN case information was invalid
            print(user_form.errors,pro.errors)
            return HttpResponse('The given user information is in valid')

    #Return value to render the register page
    return render(request,'app/register.html',{'registered': registered,
                                                'user_form' : user_form,
                                                'profile_form': profile_form,})

# user_login
def user_login(request):

    #this is for after submitting the form, data is sent by method POST
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('logined'))
            else:
                return HttpResponse('User is not active')
        else:
            print('Some one is trying to login account:')
            print(f'username: {username}')
            print(f'password: {password}')
            return HttpResponseRedirect(reverse('user_login'))
    else:
        return render(request,'app/login.html')

# logined
def logined(request):
    return HttpResponse('Nice! You are logined')

# user_logout:

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
