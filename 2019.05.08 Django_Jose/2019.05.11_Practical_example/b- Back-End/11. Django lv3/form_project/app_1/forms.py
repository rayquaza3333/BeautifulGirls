from django import forms
from django.core import validators
from . import models


def check_for_z(value):
    if value[0].lower() !='z':
        raise forms.ValidationError("NAME NEED TO START WITH 'Z'")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label = 'Enter your email again: ')
    text = forms.CharField(widget = forms.Textarea)
    botcatcher = forms.CharField(required = False,
                                 widget = forms.HiddenInput,
                                 validators = [validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data.get('email')
        vmail = all_clean_data.get('verify_email')

        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS ARE MATCH!")

class Users(forms.ModelForm):
    #Form fields go here
    botcatcher = forms.CharField(required = False,
                                 widget = forms.HiddenInput,
                                 validators = [validators.MaxLengthValidator(0)])
    class Meta():
        model = models.Users
        fields = '__all__'
    def clean(self):
        all_clean_data = super().clean()
