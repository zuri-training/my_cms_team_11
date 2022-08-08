from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import User


class RegistrationUserForm(UserCreationForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'placeholder':'Password','name':'password','id':'password','class':'input-class_name'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password','name':'confirmpassword','id':'confirmpassword','class':'input-class_name'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
        
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder':'First Name','name':'firstName','id':'firstName','class':'input-class_name'}),
            'last_name': forms.TextInput(attrs={'placeholder':'Last Name','name':'lastName','id':'lastName','class':'input-class_name'}),
            'email': forms.EmailInput(attrs={'placeholder':'name@example.com','name':'email','id':'email','class':'input-class_name'}),
            'password1': PasswordInput(),
            'password2': PasswordInput(),
        }


class UserLoginForm(ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'placeholder':'password','name':'password','id':'password','class':'input-class_name'}))

    class Meta:
        model = User
        fields = ('email', 'password')
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder':'Email','name':'email','id':'email','class':'input-class_name'}),
            'password': PasswordInput(),
        }

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid Credentials!')
