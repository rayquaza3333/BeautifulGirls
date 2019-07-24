from reviewApp.forms import UserForm, UserProfileInformationForm

from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

# index
def index(request):
    return render(request, 'reviewApp/index.html')

# register
def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(request.POST, request.FILES)
        profile_form = UserProfileInformationForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form().save()
            user.set_password(user.password) # This active the hashing to database.
            user.save()

            profile  = profile_form.save(commit=False) #Commit = false >>> changable latter
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            register = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInformationForm()

    return render(request, 'reviewApp/register.html',
    {'user_form': user_form,
    "profile_form": profile_form,
    "registered": registered,})



# login
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('special'))
            else:
                return HttpResponse('Account is not active')
        else:
            print('Someone have tried to login and failed')
            print('Username: {}, password: {}'.format(username, password))
            return HttpResponse('Invalid login info supplied')
    else:
        return render(request, 'reviewApp/login.html')


# special
@login_required
def special(request):
    return HttpResponse('You are login. Nice!')

# logout
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
