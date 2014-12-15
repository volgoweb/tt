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
from .models import Project
from main.helper.views import JsonView

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


