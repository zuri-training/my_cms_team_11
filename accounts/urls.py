from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.login_page, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('create-an-account', views.register, name='register'),
   
   
]
