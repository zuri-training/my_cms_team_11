from django.urls import path

from . import views

app_name = 'editor'


urlpatterns = [
    path('', views.index, name='index'),
    path('view-website', views.webiste_template, name='webiste_template'),

]