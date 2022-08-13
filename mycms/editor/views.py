from django.shortcuts import render, redirect
from webella.models import user_dashboard
from django.contrib import messages
from accounts.models import User

from django.views.generic.base import TemplateView
# Create your views here.


def index(request):
    
    
    return render(request, 'editor/index.html')


def webiste_template(request):
    
    user = User.object.get(email=request.user)
    user_website_template = user_dashboard.objects.get(user=user)
    
    html_link = ''
    if user_website_template.template_style == "hannah template":
        
        html_link = 'hannah template/index.html'
        
    elif user_website_template.template_style == "couple template":
        
        html_link = 'couple template/index.html'
        
    else:
        html_link = 'editor/index.html'
    
    
    return render(request, html_link)



def hannah_resume(request):
    
    return render(request, 'hannah template/resume.html')


def hannah_contact(request):
    
    return render(request, 'hannah template/contact.html')

def hannah_index(request):
    
    return render(request, 'hannah template/index.html')


def couple_blog(request):
    
    return render(request, 'couple template/blog.html')


def couple_gallery(request):
    
    return render(request, 'couple template/gallery.html')

def couple_index(request):
    
    return render(request, 'couple template/index.html')

def editor_index(request):
    
    return render(request, 'editor/index.html')


class PreView(TemplateView):
    
    # template_name = 'editor/blank.html'
    
    def get_template_names(self):
        user = User.object.get(email=self.request.user)
        user_website_template = user_dashboard.objects.get(user=user)
        
        if user_website_template.template_style == "hannah template":
        
            template_name = 'hannah template/index.html'
        
        else:
        
            template_name = 'couple template/index.html'
    
        return [template_name]