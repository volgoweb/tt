# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponse
from django.views.generic import ListView

def front_page(request):
    return render_to_response('index.html', {})
    # return HttpResponse('Main page')
