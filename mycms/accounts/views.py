from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout

from .models import User
from webella.models import user_dashboard

# Create your views here.
from .forms import RegistrationUserForm, UserLoginForm


def register(request):
    context = {}
    if request.POST:
        registration_form = RegistrationUserForm(request.POST)
        
        if registration_form.is_valid():
            user_email= registration_form.cleaned_data['email']
            request.session['user_email'] = user_email
            registration_form.save()
            messages.success(request, 'Registration successful!')
            
            return redirect('webella:on_boarding')

        context['registration_form'] = registration_form
        
    else:
        registration_form = RegistrationUserForm()
        context['registration_form'] = registration_form
    return render(request, 'accounts/register.html', context)


def login_page(request):
    context = {}
    if request.POST:
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            email = request.POST['email']
            password = request.POST['password']

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                user_dashboard_dets = user_dashboard.objects.get(user=user)
                
            
                return redirect('webella:dashboard')
                
            
        else:
            context['login_form'] = login_form

    else:
        login_form = UserLoginForm()
        context['login_form'] = login_form
 
    return render(request, 'accounts/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('accounts:login')


def forgot_password(request):
    
    
    return render(request, 'accounts/forgotpassword.html')
