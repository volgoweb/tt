from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from main.helper.views import ModelsInfoViewMixin
from rest_framework import viewsets
from rest_framework.decorators import api_view

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskModelsInfoView(ModelsInfoViewMixin):
    models = [Task,]

