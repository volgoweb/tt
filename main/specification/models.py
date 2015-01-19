# -*- coding: utf-8 -*-
from django.db import models

from main.helper.models import (
    TitleAndSlugFields,
    CreatedUpdatedField,
    DescField,
)


class Specification(TitleAndSlugFields, \
    CreatedUpdatedField, \
    DescField, \
    models.Model):
    """
    Модель для хранения технического задания на разработку либо частей веб-проектов, либо проекта целиком.
    Техническое задание имеет иеррархичную структуру.
    """
    STATUS_NEW    = 1
    STATUS_CLOSED = 46
    STATUSES      = {
        STATUS_NEW  : u'Новая',
        STATUS_CLOSED  : u'Сделана и выложена на продакшен',
    }
    status = models.IntegerField(choices = STATUSES.items(), verbose_name = u'Статус', default = STATUS_NEW)
    release = models.ForeignKey('release.Release', related_name = 'specification_release', verbose_name = u'Релиз', help_text = u'Релиз, в котором планируется выполнить данное ТЗ')


