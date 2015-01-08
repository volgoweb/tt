# -*- coding: utf-8 -*-
from rest_framework.decorators import detail_route, list_route
from rest_framework import viewsets
from rest_framework.response import Response
from django.views.generic import TemplateView

from main.helper.views import ModelsInfoViewMixin
from main.helper.models import ModelFieldsAccessTypeMixin
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
        return context


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

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


class TaskModelsInfoView(ModelsInfoViewMixin):
    models = [Task,]
