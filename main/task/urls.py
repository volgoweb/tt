# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import routers

from .views import TaskViewSet, TaskModelsInfoView, TaskMainPage
from main.helper.models import ModelFieldsAccessTypeMixin

router = routers.DefaultRouter()
router.register(r'', TaskViewSet)

urlpatterns = patterns('',
    url(r'^$', login_required(TaskMainPage.as_view()), name='task__main_page'),
    url(r'^get-models/$', TaskModelsInfoView.as_view(), name='task__get_models'),
    url(r'^rest', include(router.urls), name='task__rest'),
)
