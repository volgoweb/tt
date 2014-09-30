# -*- coding: utf-8 -*-
from .models import Task
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import User
from main.account.models import Account

class AddTaskChoicesRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        assert False
        response = super(AddTaskChoicesRenderer, self).render(response_data, accepted_media_type, renderer_context)
        return response_data

class ChoicesFieldsMixin(object):
    '''
    Перед сериализацией вместо значения формирует словарь, содержащий словарь возможных значений, текущий ключ и название значения.
    '''
    def from_native(self, data, files=None):
        for f in self.Meta.choices_fields:
            data.update({
                f: data.get(f).get('value')
            })
        return super(ChoicesFieldsMixin, self).from_native(data, files)



class TaskSerializer(ChoicesFieldsMixin, serializers.ModelSerializer):
    # status2 = serializers.CharField()
    # status_human = serializers.Field(source = 'get_human_status')

    class Meta():
        model = Task
        renderer_classes = (AddTaskChoicesRenderer,)
        fields = ('id', 'title', 'desc', 'priority', 'status', 'performer',)
        choices_fields = ('priority', 'status', 'performer',)

    def transform_priority(self, obj, value):
        return {
            'value': value,
            'title': value,
            'choices': Task.PRIORITY_CHOICES,
        }

    def transform_status(self, obj, value):
        return {
            'value': value,
            'title': Task.STATUS_CHOICES.get(value),
            'choices': Task.STATUS_CHOICES,
        }

    def transform_performer(self, obj, value):
        try:
            user = Account.objects.get(pk = value)
            title = user.get_full_fio()
        except:
            title = ''
        users_choices = dict([(u.id, u.get_full_fio()) for u in Account.objects.all().values('id', 'email', 'first_name', 'last_name', 'middle_name')])
        return {
            'value': str(value),
            'title': title,
            'choices': users_choices,
        }
