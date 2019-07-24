from django import forms
from django.contrib.auth.models import User
from massApp import UserProfile

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fileds =['username', 'password', 'email']

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = '__all__'
