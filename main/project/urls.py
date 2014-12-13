from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from main.project.views import *
from django.views.generic import TemplateView
from .views import JsonProject

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name = 'project/projects_list.html'), name='projects_list_page'),
    url(r'^json/$', JsonProject.as_view(), name='json'),
)
