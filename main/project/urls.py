from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from main.project.views import *
from django.views.generic import TemplateView
from rest_framework import routers

from .views import ProjectViewSet

router = routers.DefaultRouter()
router.register(r'', ProjectViewSet)

urlpatterns = patterns('',
    url(r'^$', login_required(TemplateView.as_view(template_name = 'project/projects_list.html')), name='projects_list_page'),
    # url(r'^get-models/$', login_required(ProjectModelsInfoView.as_view()), name='get_models'),
    url(r'^rest', include(router.urls), name='rest'),
)
