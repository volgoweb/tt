# -*- coding: utf-8 -*-
from django.db import models

from main.helper.models import (
    TitleAndSlugFields,
    CreatedUpdatedField,
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
    STATUS_IN_QUEUE = 1
    STATUS_IN_WORK    = 2
    STATUS_DONE = 3
    STATUS_SENDED_TO_PRODUCTION = 4
    STATUSES      = {
        STATUS_IN_QUEUE  : u'В очереди',
        STATUS_IN_WORK  : u'В работе',
        STATUS_READY  : u'Готов',
        STATUS_SENDED_TO_PRODUCTION  : u'Готов и выложен на продакшен',
    }
    status = models.IntegerField(choices = STATUSES.items(), verbose_name = u'Статус', default = STATUS_IN_QUEUE)
