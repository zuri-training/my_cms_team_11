from django.shortcuts import render, redirect
from webella.models import user_dashboard
from django.contrib import messages
from accounts.models import User
# Create your views here.


def index(request):
    
    
    return render(request, 'hannah template/index.html')

# Create your views here.

