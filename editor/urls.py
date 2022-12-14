from django.urls import path


from . import views
from django.views.generic import TemplateView
# from webella.models import user_dashboard

# from webella.views import on_boarding

app_name = 'editor'


urlpatterns = [
    
    path('preview', views.PreView.as_view(), name='preview'),
    path('view-website', views.PreView.as_view(), name='webiste_template'),
    path('resume', views.hannah_resume, name='hannah_resume'),
    path('contact', views.hannah_contact, name='hannah_contact'),
    path('blog', views.couple_blog, name='couple_blog'),
    path('gallery', views.couple_gallery, name='couple_gallery'),
    path('home_hannah', views.hannah_index, name='hannah_home'),
    path('home_couple', views.couple_index, name='couple_home'),
    path('', views.editor_index, name='editor_index'),
    path('getspecs', views.getTemplateSpecs, name="getTemplateSpecs"),
    path('postspecs', views.postTemplateSpecs, name="postTemplateSpecs"),

]