from django.urls import path

from . import views
from django.views.generic import TemplateView
from webella.models import user_dashboard




app_name = 'editor'


urlpatterns = [
    path('', views.index, name='index'),
    path('preview', TemplateView.as_view(template_name="couple template/index.html"), name='preview'),
    path('view-website', views.webiste_template, name='webiste_template'),
    path('resume', views.hannah_resume, name='hannah_resume'),
    path('contact', views.hannah_contact, name='hannah_contact'),
    path('blog', views.couple_blog, name='couple_blog'),
    path('gallery', views.couple_gallery, name='couple_gallery'),
    path('home_hannah', views.hannah_index, name='hannah_home'),
    path('home_couple', views.couple_index, name='couple_home'),
    path('editor', views.editor_index, name='editor_home'),

]