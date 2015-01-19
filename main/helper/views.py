# -*- coding:utf-8 -*-
import json
import datetime
from django.shortcuts import render, render_to_response
from django.http import Http404, HttpResponse
from django.template import RequestContext
from django.views.generic import View
from django.contrib.auth.models import User
from django.core import serializers

class JsonView(View):
    '''
    Представления для обработки аяксов запросов от фронтенда моделей и коллекций.
    '''

    def queryset(self, request, **kwargs):
        return self.model.objects.all()

    def get(self, request, id = None, **kwargs):
        '''
        Обработка http-запросов метода get.
        Возвращает либо объект модели, либо список объектов.
        '''
        if id:
            obj = get_object_or_404(self.queryset(request, **kwargs), id = id)
            return self.get_object_detail(request, obj)
        else:
            return self.get_collection(request, **kwargs)

    def get_model_fields(self, obj):
        '''
        Возвращает словарь значений полей модели.
        '''
        fields = {}
        for f in self.model._meta.fields:
            value = getattr(obj, f.name)
            # if isinstance(value, datetime.date):
            #     value = self.date_field_to_json(value)
            # elif isinstance(value, datetime.datetime):
            #     value = self.datetime_field_to_json(value)
            # elif isinstance(value, User):
            #     value = self.user_field_to_json(value)
            fields[f.name] = value
        return fields

    def user_field_to_json(self, value):
        fields = {}
        for f in value._meta.fields:
            v = getattr(value, f.name)
            # if isinstance(v, datetime.date):
            #     v = self.date_field_to_json(v)
            # elif isinstance(v, datetime.datetime):
            #     v = self.datetime_field_to_json(v)
            fields[f.name] = v
        # return json.dumps(fields)
        return serializers.serialize('json', fields)

    def date_field_to_json(self, value):
        return value.strftime('%d.%m.%Y')

    def datetime_field_to_json(self, value):
        return value.strftime('%d.%m.%Y %h:%i')

    def model_to_json(self, obj):
        '''
        Конвертация словаря значений модели в json формат.
        '''
        # fields = self.get_model_fields(obj)
        # return json.dumps(fields)
        return serializers.serialize('json', obj)

    def get_object_detail(self, request, obj):
        '''
        Возвращает объект модели в json-формате.
        '''
        return HttpResponse(self.model_to_json(obj), content_type = 'application/json')

    def get_collection(self, request, **kwargs):
        '''
        Возвращает список объектов указанной в запросе модели в json-формате.
        '''
        objs = self.queryset(request, **kwargs)
        return HttpResponse(serializers.serialize('json', objs))

    def put(self, request, id = None, **kwargs):
        '''
        Общий метод сохранения существующего или создание нового объекта модели.
        '''
        if id:
            obj = get_object_or_404(self.queryset(request), id = id)
            return self.update_object(request, obj)
        else:
            return self.add_object(request)

    def get_data_from_request(self, request):
        '''
        Извлекает из request словарь полученных от backbone значений полей модели и возвращает его.
        '''
        try:
            return json.loads(request.body if hasattr(request, 'body') else request.raw_post_data)
        except ValueError:
            return HttpResponseBadRequest('Parse JSON error.')

    def add_object(self, request):
        '''
        Создание новой модели.
        '''
        data = self.get_data_from_request(request)
        model_form = self.get_model_form(request, data = data)
        if model_form.is_valid():
            obj = model_form.save()
            return self.get_object_detail(request, obj)
        else:
            return HttpResponseBadRequest(json.dumps(model_form.errors), content_type='application/json')

    def update_object(self, request, obj):
        '''
        Изменение существующей модели.
        '''
        data = self.get_data_from_request(request)
        model_form = self.get_model_form(request, data = data, instance = obj)
        if model_form.is_valid():
            obj = model_form.save()
            return self.get_object_detail(request, obj)
        else:
            return HttpResponseBadRequest(json.dumps(model_form.errors), content_type='application/json')

    def get_model_form(self, request, data = None, instance = None):
        '''
        Получение формы текущей модели.
        '''
        model_form = modelform_factory(self.model)
        return model_form(data, instance = instance)


class ModelsInfoViewMixin(View):
    models = []

    def get(self, request, **kwargs):
    # def define_verbose_names(self):
        '''
        Обработка http-запросов метода get.
        Возвращает информацию о модели.
        '''
        info = {}
        for m in self.models:
            info[m.__name__] = {
                'fields_verbose_names': {},
                'fields_choices': {},
            }
            for f in m._meta.fields:
                info[m.__name__]['fields_verbose_names'][f.name] = f.verbose_name
                # if f.name =='performer':
                #     dir_f = dir(f)
                #     choices = f.get_choices_default()
                #     choices2 = f.get_choices()
                #     cl = f.__class__.__name__
                #     assert False
                # if f.__class__.__name__ == 'ForeignKey':
                #     choices = f.get_choices()
                # else
                #     choices = getattr(f, 'choices', [])
                try:
                # if f.name =='performer':
                    choices = f.get_choices()
                    del(choices[0])
                    info[m.__name__]['fields_choices'][f.name] = dict(choices)
                except:
                    pass

        return HttpResponse(json.dumps(info))

