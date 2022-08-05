from django.shortcuts import render, redirect
from .models import user_dashboard

from .forms import OnboardingForm
from django.contrib import messages

from accounts.models import User
# Create your views here.


def landing_page(request):
    
    
    return render(request, 'webella/landing.html')


def on_boarding(request):
    context = {}
   
    if request.session.has_key('user_email'):
        user_email = request.session['user_email']
        context['email'] = user_email  
        if request.method == 'POST':
            
            onboarding_form = OnboardingForm(request.POST)
            if onboarding_form.is_valid():
                dets = onboarding_form.save(commit=False)
                dets.user = User.object.get(email=user_email)
                dets.save()
                
                del request.session['user_email']
                
                return redirect('accounts:login')  
            else:
                messages.error(request, 'Error saving form')
            
    context['on_boarding_form'] = OnboardingForm()

    return render(request, 'webella/on-boarding.html', context)

def blog_dashboard(request):
    context = {}
    
       
    
    
    return render(request, 'webella/blog-dashboard.html')


def portfolio_dashboard(request):
    context = {}
    
       
    
    
    return render(request, 'webella/portfolio-dashboard.html')