from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm

# Import for login, logout
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

#Register

def index(request):
    return render(request,'index.html',{})

def register(request):

    registered = False

    if request.method == "POST":

        user_form = UserForm(request.POST,request.FILES)
        profile_form = UserProfileInfoForm(request.POST,request.FILES)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save() #This save data to database as modek and
                                    #return the model
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            profile.save()

            registered = True

            return render(request,'register.html',{'register':register,
                                                    'user_form':user_form,
                                                    'profile_form':profile_form,})

        else:
            print(user_form.errors, profile_form.errors)
            return HttpResponse('The user data is unvalid, please check again')

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'register.html',{'register':register,
                                            'user_form':user_form,
                                            'profile_form':profile_form,})

#special
@login_required
def special(request):
    return HttpResponse('Nice, you are logined')

#user_login
def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password  = request.POST.get('password')

        user = authenticate(username = username, password = password) #So this return a Boolean value and other users
                                                                    # information

        if user:
            if user.is_active:
                 login(request,user)
                 return HttpResponseRedirect(reverse('special'))
            else:
                return HttpResponse('User is not active')
        else:
            print('Someone is trying to login to this account')
            print(f'username: {username}')
            print(f'password: {password}')
            return HttpResponse('The user information is invalid')
    else:
        return render(request,'login.html',{})

#user_logout
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
