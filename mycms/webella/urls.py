from django.urls import path
<<<<<<< HEAD
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('support/', views.docs, name= 'docs'),
    path('templates/', views.templates, name = 'templates')
]

=======

from . import views

app_name = 'webella'


urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
>>>>>>> main
