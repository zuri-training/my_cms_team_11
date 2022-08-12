from django.shortcuts import render, redirect
from .models import user_dashboard
from django.contrib.auth import authenticate, login, logout

from .forms import OnboardingForm
from django.contrib import messages

from accounts.models import User
# Create your views here.


def index(request):
    
    
    return render(request, 'webella/index.html')


def on_boarding(request):
    context = {}
   
    if request.session.has_key('user_email'):
        user_email = request.session['user_email']
        user = User.object.get(email=user_email)
        
        blog_templates = ['blue blog']
        portfolio_templates = ['nude portfolio']
        
        context['email'] = user_email  
        if request.method == 'POST':
            
            user_template_choice = request.POST['template-style']
            
            print(user_template_choice)
            print(user_email)
            
            
            if user_template_choice in blog_templates:
                
                t = user_dashboard(template_style=user_template_choice, website_type="B", user=user)
                t.save()
            
            else:
                
                t = user_dashboard(template_style=user_template_choice, website_type="P", user=user)
                t.save()

            login(request, user)
            print(request.user)
            user_details = User.object.get(email=request.user)
    
            context['user_details'] = user_details
            
            return render(request, 'webella/dashboard.html', context)  
        
            # else:
            #     messages.error(request, 'Error saving form')
            
    context['on_boarding_form'] = OnboardingForm()

    return render(request, 'webella/on-boarding.html', context)

def dashboard(request):
    context = {}
    print(request.user)
    user_details = User.object.get(email=request.user)
    
    context['user_details'] = user_details
       
    
    
    return render(request, 'webella/dashboard.html', context)


