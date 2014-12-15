# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _
from main.helper.models import (
    EntityBaseManager,
    EntityBaseFields,
    TitleAndSlugFields,
    DescField,
)
from main.account.models import Account

class ProjectManager(EntityBaseManager):
    pass

class Project(EntityBaseFields, TitleAndSlugFields, DescField):
    '''
    Проект.
    '''
    testers = models.ManyToManyField(Account, verbose_name = u'Тестировщики', related_name = 'task_testers', blank = True, null = True)
    managers = models.ManyToManyField(Account, verbose_name = u'Менеджеры', related_name = 'task_managers', blank = True, null = True)
    clients = models.ManyToManyField(Account, verbose_name = u'Клиенты', related_name = 'task_clients', blank = True, null = True)
    designers = models.ManyToManyField(Account, verbose_name = u'Дизайнеры', related_name = 'task_designers', blank = True, null = True)
    members = models.ManyToManyField(Account, verbose_name = u'Участники', related_name = 'task_memebers', blank = True, null = True)


    objects = EntityBaseManager()

    class Meta():
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

