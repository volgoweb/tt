# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

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
    testers = models.ManyToManyField('account.Account', verbose_name = u'Тестировщики', related_name = 'task_testers', blank = True, null = True)
    managers = models.ManyToManyField('account.Account', verbose_name = u'Менеджеры', related_name = 'task_managers', blank = True, null = True)
    clients = models.ManyToManyField('account.Account', verbose_name = u'Клиенты', related_name = 'task_clients', blank = True, null = True)
    designers = models.ManyToManyField('account.Account', verbose_name = u'Дизайнеры', related_name = 'task_designers', blank = True, null = True)
    members = models.ManyToManyField('account.Account', verbose_name = u'Участники', related_name = 'task_memebers', blank = True, null = True)
    last_release = models.ForeignKey('release.Release', related_name = 'project_last_release', blank = True, null = True, verbose_name = u'Предыдущий релиз')
    next_release = models.ForeignKey('release.Release', related_name = 'project_next_release', blank = True, null = True, verbose_name = u'Следующий релиз')


    objects = EntityBaseManager()

    class Meta():
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def get_absolute_url(self):
        return reverse('project:project_detail', kwargs={'project_id': self.pk,})
