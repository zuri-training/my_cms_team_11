from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import User


class RegistrationUserForm(UserCreationForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='password', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')
        widgets = {
            'first_name': TextInput(),
            'last_name': TextInput(),
            'email': EmailInput(),
            'password1': PasswordInput(),
            'password2': PasswordInput(),
        }


class UserLoginForm(ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'password')
        widgets = {
            'email': EmailInput(),
            'password': PasswordInput()
        }

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid Credentials!')
