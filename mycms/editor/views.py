from django.shortcuts import render, redirect
from webella.models import user_dashboard
from django.contrib import messages
from accounts.models import User
# Create your views here.


def index(request):
    
    
    return render(request, 'editor/index.html')


def webiste_template(request):
    
    user = User.object.get(email=request.user)
    user_website_template = user_dashboard.objects.get(user=user)
    
    html_link = ''
    if user_website_template.website_type == "P":
        
        html_link = 'hannah template/index.html'
    
    else:
        html_link = 'couple template/index.html'
    
    
    return render(request, html_link)

