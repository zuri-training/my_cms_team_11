from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from webella.models import user_dashboard
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accounts.models import User
from django.forms.models import model_to_dict
import re

from .models import hannahTemplate

from django.views.generic.base import TemplateView
# Create your views here.



@login_required
def editor_index(request):
    context = {}
    user = User.object.get(email=request.user)
    user_website_template = user_dashboard.objects.get(user=user)
    
    context['user_website_template'] = user_website_template
    
    return render(request, 'editor/index.html', context)


@login_required
def webiste_template(request):
    
    context = {}
    user = User.object.get(email=request.user)
    user_website_template = user_dashboard.objects.get(user=user)
    
    html_link = ''
    if user_website_template.template_style == "hannah template":
        
        html_link = 'hannah template/index.html'
        
    elif user_website_template.template_style == "couple template":
        
        html_link = 'couple template/index.html'
        page_data = hannahTemplate.objects.get(user=user)
        
        context['page_data'] = page_data
        print("pleaseeeeeeeeeee", context)  
        
    else:
        html_link = 'editor/index.html'
    
    
    return render(request, html_link, context)



@login_required
def hannah_resume(request):
    
    return render(request, 'hannah template/resume.html')


@login_required
def hannah_contact(request):
    
    return render(request, 'hannah template/contact.html')


@login_required
def hannah_index(request):
    context = {}
    webella = User.object.get(email="webella@gmail.com")
    
    try:
        user = hannahTemplate.objects.get(user=request.user)
    except hannahTemplate.DoesNotExist:
        user = hannahTemplate.objects.get(user=webella)
        
    context['page_data'] = user
    
    return render(request, 'hannah template/index.html', context)


@login_required
def couple_blog(request):
    
    return render(request, 'couple template/blog.html')


@login_required
def couple_gallery(request):
    
    return render(request, 'couple template/gallery.html')


@login_required
def couple_index(request):
    
    return render(request, 'couple template/index.html')



@method_decorator(login_required, name='dispatch') 
class PreView(TemplateView):
    
    # template_name = 'editor/blank.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(PreView, self).get_context_data(*args, **kwargs)
    
        user = User.object.get(email=self.request.user)
        webella = User.object.get(email="webella@gmail.com")
        
        try:
            page_data = hannahTemplate.objects.get(user=user)
            
        except hannahTemplate.DoesNotExist:
            
           page_data = hannahTemplate.objects.get(user=webella)
    
        context['page_data'] = page_data
        print("pleaseeeeeeeeeee", context)
        
        return context
    
    def get_template_names(self):
        user = User.object.get(email=self.request.user)
        webella = User.object.get(email="webella@gmail.com")
        
        try:
            user_website_template = user_dashboard.objects.get(user=user)
            
        except user_dashboard.DoesNotExist:
            
           user_website_template = user_dashboard.objects.get(user=webella)
        
        if user_website_template.template_style == "hannah template":
        
            template_name = 'hannah template/index.html'
        
        elif user_website_template.template_style == "couple template":
        
            template_name = 'couple template/index.html'
    
        else: 
            template_name = 'editor/blank.html'
            
            
        return [template_name]
    
 
@login_required
def getTemplateSpecs(request): 
    
    webella = User.object.get(email="webella@gmail.com")
    
    try:
        specs = hannahTemplate.objects.get(user=request.user)

        
    except hannahTemplate.DoesNotExist:
        specs = hannahTemplate.objects.get(user=webella)
        

    specs_dict = model_to_dict(specs)
    # specs_dict['hero-img'] = specs.hero_image.url
    
    return JsonResponse({'hannah_template':specs_dict})


@login_required
def postTemplateSpecs(request):  
    
    print(request.user, "postTemp")
    

    print("whyyyy")
    print(request.POST)
    nav_text1 = request.POST.get('nav_link_1_text')
    nav_text2 = request.POST.get('nav_link_2_text')
    nav_text3 = request.POST.get('nav_link_3_text')

    page_title = request.POST.get('page_title')

    hero_text_small = request.POST.get('hero_text_small')
    hero_text_big = request.POST.get('hero_text_big')
    
    background_color = request.POST.get('background_color')
    hero_div_color = request.POST.get('hero_div_color')
    
    about_paragraph = request.POST.get('about_paragraph')
    
    user_specs = hannahTemplate.objects.get(user=request.user)
    
    print(user_specs)
    
    user_specs.nav_text1 = nav_text1
    user_specs.nav_text2 = nav_text2
    user_specs.nav_text3 = nav_text3
    user_specs.page_title = page_title
    user_specs.hero_text_small = hero_text_small
    user_specs.hero_text_big = hero_text_big
    
    user_specs.background_color = background_color
    user_specs.hero_div_color = hero_div_color
    
    user_specs.about_paragraph = about_paragraph
    
    user_specs.save()

    user_specs = hannahTemplate.objects.get(user=request.user)
    
    user_specs_dict = model_to_dict(user_specs)
        
    return JsonResponse({'response':user_specs_dict})