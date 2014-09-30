# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _
from main.helper.models import *
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from main.account.models import Account
from main.project.models import Project

class Task(EntityBaseFields, TitleField, DescField):
    '''
    Задача.
    '''
    PRIORITY_CHOICES = {v: v for v in range(-2, 3)}
    STATUS_CHOICES = {
        'new': _('New'),
        'in_work': _('In work'),
        'ready': _('Ready'),
    }

    priority = models.IntegerField(choices = PRIORITY_CHOICES.items(), verbose_name = u'Приоритет', default = 0)
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES.items(), verbose_name = u'Статус', default = 'new')
    author = models.ForeignKey(Account, verbose_name = u'Автор', related_name = 'task_author')
    developer = models.ForeignKey(Account, verbose_name = u'Разработчик', related_name = 'task_developer')
    tester = models.ForeignKey(Account, verbose_name = u'Тестировщик', related_name = 'task_tester', blank = True, null = True)
    manager = models.ForeignKey(Account, verbose_name = u'Менеджер', related_name = 'task_manager', blank = True, null = True)
    client = models.ForeignKey(Account, verbose_name = u'Клиент', related_name = 'task_client', blank = True, null = True)
    project = models.ForeignKey(Project, verbose_name = u'Проект', related_name = 'task_project', blank = True, null = True)
    # objects = models.Manager()

    class Meta():
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

