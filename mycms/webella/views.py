from django.shortcuts import render

# Create your views here.

<<<<<<< HEAD
def index(request):
    context = {}
    return render(request, 'webella/index.html', context)

def docs(request):
    context = {}
    return render(request, 'webella/docs.html', context)

def templates(request):
    context = {}
    return render(request, 'webella/gallery.html', context)

def Signup():
    pass

def Login():
    pass

=======

def landing_page(request):
    
    
    return render(request, 'webella/landing.html')


def dashboard(request):
    
    
    return render(request, 'webella/dashboard.html')
>>>>>>> main
