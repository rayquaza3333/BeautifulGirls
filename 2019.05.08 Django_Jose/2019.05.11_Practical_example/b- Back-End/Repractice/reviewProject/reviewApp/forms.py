from django import forms
from models import UserProfileInformationForm
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username', 'password', 'email')

class UserProfileInformationForm(forms.ModelForm):

    class Meta():
        model = UserProfileInformationForm
        fields = ('portfolio_site', 'profile_pic')
