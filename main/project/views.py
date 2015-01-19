# -*- coding:utf-8 -*-
import json
import datetime
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponse
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from rest_framework import viewsets

from .models import Project
from .serializers import ProjectSerializer
from main.helper.views import JsonView


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    paginate_by = 10

    def create(self, request, *args, **kwargs):
        request.DATA[u'author'] = unicode(request.user.pk)
        request.DATA[u'status'] = {
            'value': Project.STATUS_NEW,
        }
        return super(ProjectViewSet, self).create(request, *args, **kwargs)

    # @detail_route(methods=['get'])
    # def run_action(self, request, pk=None):
    #     """ Запуск действия по задаче. """
    #     project = self.object = self.get_object()
    #     action = request.GET.get('action')
    #     if action:
    #         project.run_action(action, request.user)
    #     # TODO обрабатывать неуспех
    #     serializer = self.get_serializer(project)
    #     return Response(serializer.data)

    # @list_route()
    # def projects_list(self, request):
    #     projects_list_name = request.GET.get('projects_list_name')
    #     qs = self.get_projects_list_queryset(request, projects_list_name)
    #     page = self.paginate_queryset(qs)
    #     serializer = self.get_pagination_serializer(page)
    #     return Response(serializer.data)

    # @list_route(methods=['get'])
    # def projects_list_count(self, request):
    #     projects_list_name = request.GET.get('projects_list_name')
    #     count = len(self.get_projects_list_ids(request, projects_list_name))
    #     return Response(count)

    # def get_projects_list_ids(self, request, projects_list_name):
    #     # Перевести код в фабрику
    #     CollectionClass = get_collection_class()
    #     collection_name = '{0}:uid_{1}'.format(projects_list_name, request.user.pk)
    #     # TODO вынести параметр кол-ва страниц в конфиг
    #     cl = CollectionClass(name=collection_name, per_page=20)
    #     ids = cl.get_items()
    #     return ids

    # def get_projects_list_queryset(self, request, projects_list_name):
    #     ids = self.get_projects_list_ids(request, projects_list_name)
    #     qs = Project.objects.filter(pk__in=ids)
    #     return qs


class ProjectsList(ListView):
    model = Project
    template_name = 'project/project_list.html'
    context_object_name = 'models'
    paginate_by = 10

    def get_queryset(self):
        return Project.objects.active()

class ProjectsMainList(ProjectsList):
    @login_required()
    def dispatch(self, request, *args, **kwargs):
        return super(ProjectsMainList, self).dispatch(request, *args, **kwargs)

def get_projects_json(request):
    models = Project.objects.all()
    return HttpResponse(json.dumps(models))

class JsonProject(JsonView):
    model = Project


