from django import forms
from app34 import models
def check_for_z(value):

    if value[0].lower() != 'z':
        raise forms.ValidationError('Name need to start with z')

class FormName(forms.Form):
    name = forms.CharField(validators =[check_for_z] )
    email = forms.EmailField()
    vmail = forms.EmailField(label = 'Enter your email again')
    text = forms.CharField(widget = forms.Textarea)

    def clean(self):
        all_cleaned_data = super().clean()
        email = all_cleaned_data.get('email')
        vmail = all_cleaned_data.get('vmail')

        if email != vmail:
            raise forms.ValidationError('MAKE SURE EMAILS ARE MATCH!')

class UserForm(forms.ModelForm):
    class Meta():
        model = models.Users
        fields = '__all__'
