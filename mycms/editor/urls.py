from django.urls import path

from . import views

app_name = 'editor'


urlpatterns = [
    path('', views.index, name='index'),
    path('view-website', views.webiste_template, name='webiste_template'),
    path('resume', views.hannah_resume, name='hannah_resume'),
    path('contact', views.hannah_contact, name='hannah_contact'),
    path('blog', views.couple_blog, name='couple_blog'),
    path('gallery', views.couple_gallery, name='couple_gallery'),
    

]