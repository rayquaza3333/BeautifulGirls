from django import forms
from .models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    # To add scensored password.
    password = forms.CharField(widget = forms.PasswordInput())

    #inherit attributes from User model
    class Meta():
        model = User
        fields = ('username','password','email')

class UserProfileInfoForm(forms.ModelForm):
    #inherit from UserProfileInfo model
    class Meta():
        model = UserProfileInfo
        fields ='__all__'
