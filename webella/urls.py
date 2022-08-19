from django.urls import path

from . import views

app_name = 'webella'


urlpatterns = [
    path('', views.index, name='index'),
    path('on-boarding/', views.on_boarding, name='on_boarding'),
    path('dashboard/', views.dashboard, name='dashboard'),

]