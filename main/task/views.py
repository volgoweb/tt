# -*- coding: utf-8 -*-
from rest_framework.decorators import detail_route, list_route
from rest_framework import viewsets
from rest_framework.response import Response
from django.views.generic import TemplateView

from main.helper.views import ModelsInfoViewMixin
from main.helper.models import ModelFieldsAccessTypeMixin
from main.helper.collection.collections import get_collection_class
from .models import Task
from .serializers import TaskSerializer


class TaskMainPage(TemplateView):
    template_name = 'task/tasks_list_page.html'

    def get_context_data(self, **kwargs):
        context = super(TaskMainPage, self).get_context_data(**kwargs)
        context['ModelFieldsAccessTypeMixin'] = {
            'FIELD_ACCESS_TYPE_DENY': ModelFieldsAccessTypeMixin.FIELD_ACCESS_TYPE_DENY,
            'FIELD_ACCESS_TYPE_VIEW': ModelFieldsAccessTypeMixin.FIELD_ACCESS_TYPE_VIEW,
            'FIELD_ACCESS_TYPE_FULL': ModelFieldsAccessTypeMixin.FIELD_ACCESS_TYPE_FULL,
        }
        # assert False
        return context


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    paginate_by = 10

    def create(self, request, *args, **kwargs):
        request.DATA[u'author'] = unicode(request.user.pk)
        request.DATA[u'status'] = {
            'value': Task.STATUS_WENT_TO_PERFORMER,
        }
        return super(TaskViewSet, self).create(request, *args, **kwargs)

    @detail_route(methods=['get'])
    def run_action(self, request, pk=None):
        """ Запуск действия по задаче. """
        task = self.object = self.get_object()
        action = request.GET.get('action')
        if action:
            task.run_action(action, request.user)
        # TODO обрабатывать неуспех
        serializer = self.get_serializer(task)
        return Response(serializer.data)


    @list_route()
    def tasks_list(self, request):
        tasks_list_name = request.GET.get('tasks_list_name')
        qs = self.get_tasks_list_queryset(request, tasks_list_name)
        page = self.paginate_queryset(qs)
        serializer = self.get_pagination_serializer(page)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def tasks_list_count(self, request):
        tasks_list_name = request.GET.get('tasks_list_name')
        count = len(self.get_tasks_list_ids(request, tasks_list_name))
        return Response(count)

    def get_tasks_list_ids(self, request, tasks_list_name):
        # Перевести код в фабрику
        CollectionClass = get_collection_class()
        collection_name = '{0}:uid_{1}'.format(tasks_list_name, request.user.pk)
        # TODO вынести параметр кол-ва страниц в конфиг
        cl = CollectionClass(name=collection_name, per_page=20)
        ids = cl.get_items()
        return ids

    def get_tasks_list_queryset(self, request, tasks_list_name):
        ids = self.get_tasks_list_ids(request, tasks_list_name)
        qs = Task.objects.filter(pk__in=ids)
        return qs


class TaskModelsInfoView(ModelsInfoViewMixin):
    models = [Task,]
