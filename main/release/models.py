# -*- coding: utf-8 -*-
from django.db import models

from main.helper.models import (
    TitleAndSlugFields,
    CreatedUpdatedField,
    DateField,
    DescField,
)


class Release(TitleAndSlugFields, \
    CreatedUpdatedField, \
    DateField, \
    DescField, \
    models.Model):
    """
    Модель для хранения технического задания на разработку либо частей веб-проектов, либо проекта целиком.
    Техническое задание имеет иеррархичную структуру.
    """
    STATUS_IN_QUEUE = 10
    STATUS_IN_WORK    = 20
    STATUS_READY = 30
    STATUS_TESTING = 40
    STATUS_REWORK = 50
    STATUS_READY_TO_DEPLOY = 60
    STATUS_SENDED_TO_PRODUCTION = 70
    STATUSES      = {
        STATUS_IN_QUEUE  : u'В очереди',
        STATUS_IN_WORK  : u'В работе',
        STATUS_READY  : u'Готов',
        STATUS_TESTING  : u'Тестируется',
        STATUS_REWORK  : u'Доработка',
        STATUS_READY_TO_DEPLOY  : u'Готов к деплою',
        STATUS_SENDED_TO_PRODUCTION  : u'Готов и выложен на продакшен',
    }
    status = models.IntegerField(choices=STATUSES.items(), verbose_name=u'Статус', default=STATUS_IN_QUEUE)
    project = models.ForeignKey('project.Project', related_name='release_project')
