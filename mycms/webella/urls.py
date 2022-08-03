from django.urls import path

from . import views

app_name = 'webella'


urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('dashboard/', views.dashboard, name='dashboard'),
]