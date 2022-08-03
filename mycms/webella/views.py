from django.shortcuts import render

# Create your views here.

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

