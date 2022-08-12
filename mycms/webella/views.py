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
        context['email'] = user_email  
        if request.method == 'POST':
            
            # user_site_dets = user_dashboard.objects.create(template_style="", website_type="", user=user)
            
            # login(request, user)
            
            return redirect('webella:dashboard')  
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


