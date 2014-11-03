# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from main.helper.models import *
from main.helper.models import ModelFieldsAccessTypeMixin
from main.account.models import Account
from main.project.models import Project

class TaskFieldsAccessTypeMixin(ModelFieldsAccessTypeMixin):
    """
    Определение и получение прав на каждое поле задачи.
    """

    def get_field_priority_access_type(self, user):
        if user.id in (self.author.id, self.manager.id) or user.is_superuser:
            return self.FIELD_ACCESS_TYPE_FULL
        else:
            return self.FIELD_ACCESS_TYPE_VIEW

    def get_field_status_access_type(self, user):
        if user.id in (self.author.id, self.manager.id) or user.is_superuser:
            return self.FIELD_ACCESS_TYPE_FULL
        else:
            return self.FIELD_ACCESS_TYPE_VIEW

    def get_field_performer_access_type(self, user):
        if user.id in (self.author.id, self.manager.id) or user.is_superuser:
            return self.FIELD_ACCESS_TYPE_FULL
        else:
            return self.FIELD_ACCESS_TYPE_VIEW


class Task(EntityBaseFields, TitleField, DescField, TaskFieldsAccessTypeMixin):
    """
    Задача.
    """

    PRIORITY_CHOICES = {
        -2: u'Совсем не срочно',
        -1: u'Не срочно',
        0: u'Обычно',
        1: u'Срочно',
        2: u'Очень срочно',
    }

    IMPORTANCE_CHOICES = {
        -2: u'Совсем не важно',
        -1: u'Не важно',
        0: u'Обычно',
        1: u'Важно',
        2: u'Очень важно',
    }

    STATUS_NEW_CHOICE = 'new'
    STATUS_IN_QUEUE_CHOICE = 'in_queue'
    STATUS_REJECTED_CHOICE = 'rejected'
    STATUS_IN_WORK_CHOICE = 'in_work'
    STATUS_READY_CHOICE = 'ready'
    STATUS_TESTED_CHOICE = 'tested'
    STATUS_ACCEPTED_BY_MANAGER_CHOICE = 'accepted_by_manager'
    STATUS_ACCEPTED_BY_CLIENT_CHOICE = 'accepted_by_client'
    STATUS_CLOSED_CHOICE = 'closed'
    STATUS_CHOICES = {
        STATUS_NEW_CHOICE: u'Новая',
        STATUS_IN_QUEUE_CHOICE: u'В очереди',
        STATUS_REJECTED_CHOICE: u'Отклонена',
        STATUS_IN_WORK_CHOICE: u'В работе',
        STATUS_READY_CHOICE: u'Решена',
        STATUS_TESTED_CHOICE: u'Проверена тестировщиком',
        STATUS_ACCEPTED_BY_MANAGER_CHOICE: u'Принята менеджером',
        STATUS_ACCEPTED_BY_CLIENT_CHOICE: u'Принята клиентом',
        STATUS_CLOSED_CHOICE: u'Закрыта',
    }

    priority = models.IntegerField(choices = PRIORITY_CHOICES.items(), verbose_name = u'Срочность', default = 0)
    importance = models.IntegerField(choices = IMPORTANCE_CHOICES.items(), verbose_name = u'Важность', default = 0)
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES.items(), verbose_name = u'Статус', default = 'new')
    author = models.ForeignKey(Account, verbose_name = u'Автор', related_name = 'task_author')
    performer = models.ForeignKey(Account, verbose_name = u'Исполнитель', related_name = 'task_performer', blank = True, null = True)
    developer = models.ForeignKey(Account, verbose_name = u'Разработчик', related_name = 'task_developer', blank = True, null = True)
    tester = models.ForeignKey(Account, verbose_name = u'Тестировщик', related_name = 'task_tester', blank = True, null = True)
    manager = models.ForeignKey(Account, verbose_name = u'Менеджер', related_name = 'task_manager', blank = True, null = True)
    client = models.ForeignKey(Account, verbose_name = u'Клиент', related_name = 'task_client', blank = True, null = True)
    project = models.ForeignKey(Project, verbose_name = u'Проект', related_name = 'task_project', blank = True, null = True)

    # objects = models.Manager()

    class Meta():
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def get_available_actions(self, user):
        """
        Возвращает список доступных действий,
        которые можно выполнить над задачей при текущих значениях полей
        и для указанного пользователя.
        """
        actions = []

        all_actions = {
            'go_to_testing': {
                'name': 'go_to_testing',
                'title': u'Отправить на тестирование',
            },
            'go_to_accepting_by_manager': {
                'name': 'go_to_accepting_by_manager',
                'title': u'Отправить на проверку менеджеру',
            },
            'go_to_accepting_by_client': {
                'name': 'go_to_accepting_by_client',
                'title': u'Отправить на проверку клиенту',
            },
            'reject_work': {
                'name': 'reject_work',
                'title': u'Отправить на доработку',
            }
        }

        if self.status == self.STATUS_IN_WORK_CHOICE:
            actions.append(all_actions['go_to_testing'])
        elif self.status == self.STATUS_READY_CHOICE:
            actions.append(all_actions['reject_work'])
            actions.append(all_actions['go_to_accepting_by_manager'])
        elif self.status == self.STATUS_TESTED_CHOICE:
            actions.append(all_actions['reject_work'])
            actions.append(all_actions['go_to_accepting_by_client'])
        return actions

    def get_field_available_choices(self, user, field_name):
        """
        Возвращает словарь допустимых значений
        указанному пользователю для указанного поля.
        """
        method_name = 'get_{0}_field_available_choices'.format(field_name)
        method = getattr(self, method_name)
        if callable(method):
            return method(user)

    def run_action(self, action, user):
        """
        Выполняет указанное действие над объектом модели.
        """
        method = getattr(self, action, None)
        if callable(method):
            return method(user)

    def complete(self, user):
        """
        Помечает задачу как выполненную исполнителем.
        """
        self.status = self.STATUS_READY_CHOICE
        self.save()

    def go_to_testing(self, user):
        """
        Помечает задачу как ожидающую тестирования.
        """
        self.complete(user)
        self.save()

    def go_to_checking(self, user):
        """
        Помечает задачу как ожидающую проверки постановщиком.
        """
        self.status = self.STATUS_TESTED_CHOICE
        self.save()

    def go_to_accepting_by_manager(self, user):
        self.status = self.STATUS_TESTED_CHOICE
        self.save()

    def go_to_accepting_by_client(self, user):
        self.status = self.STATUS_ACCEPTED_BY_MANAGER_CHOICE
        self.save()

    def reject_work(self, user):
        self.status = self.STATUS_REJECTED_CHOICE
        self.save()
