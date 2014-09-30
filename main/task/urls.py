# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework import routers
from .views import TaskViewSet, TaskModelsInfoView
from django.views.decorators.csrf import ensure_csrf_cookie

router = routers.DefaultRouter()
router.register(r'', TaskViewSet)

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name = 'task/tasks_list_page.html'), name='task__tasks_list_page'),
    url(r'^get-models/$', TaskModelsInfoView.as_view(), name='task__get_models'),
    url(r'^rest', include(router.urls), name='task__rest'),
)
