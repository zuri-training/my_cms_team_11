from django.shortcuts import render

# Create your views here.


def landing_page(request):
    
    
    return render(request, 'webella/landing.html')


def dashboard(request):
    
    
    return render(request, 'webella/dashboard.html')