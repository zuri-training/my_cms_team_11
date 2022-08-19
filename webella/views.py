from django.shortcuts import render, redirect
from .models import user_dashboard
from editor.models import hannahTemplate
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from .forms import OnboardingForm
from django.contrib import messages

from accounts.models import User
# Create your views here.

user_dets = {}


def index(request):
    
    
    return render(request, 'webella/index.html')


@login_required
def on_boarding(request):
    context = {}
   
    # if request.session.has_key('user_email'):
        
    #     print(request.session)
    #     user_email = request.session['user_email']
    user = User.object.get(email=request.user)
    print(request.user)
    
    blog_templates = ['couple template']
    portfolio_templates = ['hannah template']
    
    if request.method == 'POST':
        
        user_template_choice = request.POST['template-style']
        
        print(user_template_choice)
        # print(user_email)
        
        
        if user_template_choice in blog_templates:
            
            t = user_dashboard.objects.get(user=user)
            t.template_style = user_template_choice
            t.website_type = "B"
            t.save()
        
        else:
            
            t = user_dashboard.objects.get(user=user)
            t.template_style = user_template_choice
            t.website_type = "P"
            t.save()

            hannahTemplate.objects.get_or_create(user=user)
            
    
        context['user_details'] = user
        user_dets['user'] = user
        
        return redirect('editor:editor_index')  
        
            # else:
            #     messages.error(request, 'Error saving form')
            
    context['on_boarding_form'] = OnboardingForm()

    return render(request, 'webella/on-boarding.html', context)


@login_required
def dashboard(request):
    context = {}
    print(request.user)
    user_details = User.object.get(email=request.user)
    
    context['user_details'] = user_details
       
    
    
    return render(request, 'webella/dashboard.html', context)


