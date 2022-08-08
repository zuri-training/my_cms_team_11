from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import User


class RegistrationUserForm(UserCreationForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'placeholder':'Password','name':'Name','id':'common_id_for_imputfields','class':'input-class_name'}))
    password2 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'placeholder':'Verify Password','name':'Name','id':'common_id_for_imputfields','class':'input-class_name'}))

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')
        widgets={
                   "name":forms.TextInput(attrs={'placeholder':'Name','name':'Name','id':'common_id_for_imputfields','class':'input-class_name'}),
                   "description":forms.TextInput(attrs={'placeholder':'description','name':'description','id':'common_id_for_imputfields','class':'input-class_name'}),
                }  
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder':'First Name','name':'Name','id':'common_id_for_imputfields','class':'input-class_name'}),
            'last_name': forms.TextInput(attrs={'placeholder':'Last Name','name':'Name','id':'common_id_for_imputfields','class':'input-class_name'}),
            'email': forms.EmailInput(attrs={'placeholder':'Email','name':'Name','id':'common_id_for_imputfields','class':'input-class_name'}),
            'password1': password1,
            'password2': password2,
        }


class UserLoginForm(ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'password')
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder':'Email','name':'Name','id':'common_id_for_imputfields','class':'input-class_name'}),
            'password': password,
        }

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid Credentials!')
