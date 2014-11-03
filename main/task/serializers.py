# -*- coding: utf-8 -*-
from django.db import models
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import User

from main.helper.models import ModelFieldsAccessTypeMixin
from main.account.models import Account
from .models import Task


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
        if data:
            for f in self.Meta.choices_fields:
                data.update({
                    f: data.get(f).get('value')
                })
        return super(ChoicesFieldsMixin, self).from_native(data, files)


class TaskSerializer(ChoicesFieldsMixin, serializers.ModelSerializer):
    actions = serializers.SerializerMethodField('get_actions')

    class Meta():
        model = Task
        renderer_classes = (AddTaskChoicesRenderer,)
        # fields = ('id', 'title', 'desc', 'priority', 'status', 'performer',)
        choices_fields = ('priority', 'status', 'performer',)

    def default_choices_field_transform(self, obj, value, field_name):
        access_type = obj.get_field_access_type(field_name, self.context['request'].user)
        trans_value = {
            'access_type': access_type,
        }
        if access_type != ModelFieldsAccessTypeMixin.FIELD_ACCESS_TYPE_DENY:
            get_display_method = getattr(obj, 'get_{0}_display'.format(field_name))
            trans_value.update({
                'value': value,
                'title': get_display_method() if isinstance(obj, Task) else '',
            })
        if access_type == ModelFieldsAccessTypeMixin.FIELD_ACCESS_TYPE_FULL:
            field = obj._meta.get_field_by_name(field_name)[0]
            trans_value.update({
                'choices': dict(field.choices),
            })
        return trans_value

    def transform_priority(self, obj, value):
        return self.default_choices_field_transform(obj, value, 'priority')

    def transform_status(self, obj, value):
        return self.default_choices_field_transform(obj, value, 'status')

    def transform_performer(self, obj, value):
        try:
            user = Account.objects.get(pk = value)
            title = user.get_full_fio()
        except:
            title = ''
        accounts = Account.objects.all().only('id', 'email', 'first_name', 'last_name', 'middle_name')
        users_choices = dict([(u.id, u.get_full_fio()) for u in accounts])
        return {
            'value': str(value),
            'title': title,
            'choices': users_choices,
            'access_type': obj.get_field_status_access_type(self.context['request'].user),
        }

    def get_actions(self, obj):
        request = self.context.get('request')
        if hasattr(request, 'user'):
            return obj.get_available_actions(request.user)

