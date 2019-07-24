from django import forms
from reviewApp.models import UserProfileInformation
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username', 'password', 'email')

class UserProfileInformationForm(forms.ModelForm):

    class Meta():
        model = UserProfileInformation
        fields = ('portfolio_site', 'profile_pic')
