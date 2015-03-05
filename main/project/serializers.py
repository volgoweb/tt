# -*- coding: utf-8 -*-
from django.db import models
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import User

from main.helper.models import ModelFieldsAccessTypeMixin
# from main.helper.serializers import BaseSerializer
from main.account.models import Account
from main.release.serializers import ReleaseSerializer
from .models import Project


class BaseSerializer(object):
    """
    При сериализации вместо значения поля формируется словарь
    с различными параметрами поля (тип доступа, человекопонятное значение, ...)
    """
    def default_field_transform(self, obj, value, field_name):
        # access_type = obj.get_field_access_type(field_name, user=self.context['request'].user)
        # trans_value = {
        #     'access_type': access_type,
        # }
        # if access_type != ModelFieldsAccessTypeMixin.FIELD_ACCESS_TYPE_DENY:
        trans_value = {
            'value': value,
            'title': value,
        }
        return trans_value

    def from_native(self, data, files=None):
        if data:
            for f in self.get_fields().keys():
                if f not in data:
                    continue
                value = data.get(f, {})
                if isinstance(value, dict):
                    data.update({
                        f: value.get('value', None)
                    })
        return super(BaseSerializer, self).from_native(data, files)

    def default_choices_field_transform(self, obj, value, field_name):
        '''
        Перед сериализацией вместо значения формирует словарь, содержащий словарь возможных значений, текущий ключ и название значения.
        '''
        field = obj._meta.get_field_by_name(field_name)[0]
        get_display_method = getattr(obj, 'get_{0}_display'.format(field_name))
        trans_value = {
            'value': value,
            'title': get_display_method() if isinstance(obj, Task) else '',
            'choices': dict(field.choices),
        }
        return trans_value


class ProjectSerializer(BaseSerializer, serializers.ModelSerializer):
    # actions = serializers.SerializerMethodField('get_actions')
    next_release = ReleaseSerializer()
    get_absolute_url = serializers.URLField(source='get_absolute_url')

    class Meta():
        model = Project
        # Поля с выбором значения из словаря {id: title}. 
        # При сохранении они получают вместо значения словарь {'value': id}
        choices_fields = (
            'testers',
            'managers',
            'clients',
            'designers',
            'members',
        )

    def transform_desc(self, obj, value):
        return self.default_field_transform(obj, value, 'desc')

    def transform_priority(self, obj, value):
        return self.default_choices_field_transform(obj, value, 'priority')

    def transform_user_field(self, obj, value, field_name):
        try:
            user = Account.objects.get(pk = value)
            title = user.get_full_fio()
        except:
            title = ''
        accounts = Account.objects.all().only('id', 'email', 'first_name', 'last_name', 'middle_name')
        users_choices = dict([(u.id, u.get_full_fio()) for u in accounts])
        return {
            'value': str(value or ''),
            'title': title,
            'choices': users_choices,
            # 'access_type': obj.get_field_access_type(field_name, user=self.context['request'].user),
        }

    def transform_testers(self, obj, value):
        return self.transform_user_field(obj, value, 'performer')

    def transform_managers(self, obj, value):
        return self.transform_user_field(obj, value, 'lead_programmer')

    def transform_clients(self, obj, value):
        return self.transform_user_field(obj, value, 'tester')

    def transform_designers(self, obj, value):
        return self.transform_user_field(obj, value, 'manager')

    def transform_members(self, obj, value):
        return self.transform_user_field(obj, value, 'client')

    # def get_actions(self, obj):
    #     request = self.context.get('request')
    #     if hasattr(request, 'user'):
    #         return obj.get_available_actions(request.user)
