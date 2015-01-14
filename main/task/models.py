# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.dispatch import receiver
from django.db.models.signals import post_save

from main.helper.models import *
from main.helper.models import ModelFieldsAccessTypeMixin
from main.account.models import Account
from main.project.models import Project
from .collections import TaskCollectionsFabric


class TaskFieldsAccessTypeMixin(ModelFieldsAccessTypeMixin):
    """
    Определение и получение прав на каждое поле задачи.
    """

    def get_field_desc_access_type(self, user):
        roles = self.get_user_roles(user)
        if roles & set([self.ROLE_AUTHOR, self.ROLE_MANAGER, self.ROLE_LEAD_PROGRAMMER, self.ROLE_SUPERUSER]):
            return self.FIELD_ACCESS_TYPE_FULL
        else:
            return self.FIELD_ACCESS_TYPE_VIEW

    def get_field_priority_access_type(self, user):
        return self.get_field_desc_access_type(user)

    def get_field_importance_access_type(self, user):
        return self.get_field_desc_access_type(user)

    def get_field_status_access_type(self, user):
        return self.get_field_desc_access_type(user)

    def get_field_performer_access_type(self, user):
        return self.get_field_desc_access_type(user)

    def get_field_lead_programmer_access_type(self, user):
        roles = self.get_user_roles(user)
        if roles & set([self.ROLE_AUTHOR, self.ROLE_MANAGER, self.ROLE_SUPERUSER]):
            return self.FIELD_ACCESS_TYPE_FULL
        else:
            return self.FIELD_ACCESS_TYPE_VIEW

    def get_field_tester_access_type(self, user):
        return self.get_field_performer_access_type(user)

    def get_field_manager_access_type(self, user):
        return self.get_field_lead_programmer_access_type(user)

    def get_field_client_access_type(self, user):
        return self.get_field_lead_programmer_access_type(user)


class TaskActionsMixin(object):
    ACTION_SEND_TO_PERFORMER            = 'send_to_performer'
    ACTION_REJECT_PERFORM               = 'reject_perform'
    ACTION_ADD_TO_PERFORMANCE_QUEUE     = 'add_to_performance_queue'
    ACTION_START_PERFORMANCE            = 'start_performance'
    ACTION_PAUSE_PERFORMANCE            = 'pause_performance'
    ACTION_MARK_AS_PERFORMED            = 'mark_as_performed'
    ACTION_SEND_TO_LEAD_PROGRAMMER      = 'send_to_lead_programmer'
    ACTION_ADD_TO_CODE_REVIEW_QUEUE     = 'add_to_code_review_queue'
    ACTION_START_CODE_REVIEW            = 'start_code_review'
    ACTION_SEND_TO_TESTING              = 'send_to_testing'
    ACTION_REJECT_TEST                  = 'reject_test'
    ACTION_ADD_TO_TESTING_QUEUE         = 'add_to_testing_queue'
    ACTION_START_TESTING                = 'start_testing'
    ACTION_ACCEPT_WORK_BY_TESTER        = 'accept_work_by_tester'
    ACTION_SEND_TO_CLIENT               = 'send_to_client'
    ACTION_ADD_TO_CLIENT_CHECKING_QUEUE = 'add_to_client_checking_queue'
    ACTION_START_CLIENT_CHECKING        = 'start_client_checking'
    ACTION_SEND_TO_REWORK               = 'send_to_rework'
    ACTION_ACCEPT_WORK_BY_CLIENT        = 'accept_work_by_client'
    ACTION_CLOSE_TASK                   = 'close_task'

    ACTIONS = {
        ACTION_SEND_TO_PERFORMER            : u'Отправить исполнителю',
        ACTION_REJECT_PERFORM               : u'Отказаться выполнять',
        ACTION_ADD_TO_PERFORMANCE_QUEUE     : u'В очередь',
        ACTION_START_PERFORMANCE            : u'Начать выполнение',
        ACTION_PAUSE_PERFORMANCE            : u'Пауза выполнения',
        ACTION_MARK_AS_PERFORMED            : u'Пометить как выполненное',
        ACTION_SEND_TO_LEAD_PROGRAMMER      : u'Отправить тимлиду',
        ACTION_ADD_TO_CODE_REVIEW_QUEUE     : u'В очередь',
        ACTION_START_CODE_REVIEW            : u'Начать проверку',
        ACTION_SEND_TO_TESTING              : u'Отправить на тестирование',
        ACTION_REJECT_TEST                  : u'Отказаться тестировать',
        ACTION_ADD_TO_TESTING_QUEUE         : u'В очередь',
        ACTION_START_TESTING                : u'Начать тестирование',
        ACTION_ACCEPT_WORK_BY_TESTER        : u'Ошибок не найдено',
        ACTION_SEND_TO_CLIENT               : u'Отправить заказчику',
        ACTION_ADD_TO_CLIENT_CHECKING_QUEUE : u'В очередь',
        ACTION_START_CLIENT_CHECKING        : u'Начать проверку',
        ACTION_SEND_TO_REWORK               : u'Отправить на доработку',
        ACTION_ACCEPT_WORK_BY_CLIENT        : u'Принять работу',
        ACTION_CLOSE_TASK                   : u'Завершить задачу',
    }

    def get_available_actions(self, user):
        """
        Возвращает список доступных действий,
        которые можно выполнить над задачей при текущих значениях полей
        и для указанного пользователя.
        """
        actions = {}

        roles = self.get_user_roles(user)

        for name, title in self.ACTIONS.items():
            method_name = 'has_action_{0}'.format(name)
            method = getattr(self, method_name, None)
            if callable(method):
                if method(user, roles):
                    actions.update({
                        name: title,
                    })

        return actions

    def has_action_send_to_performer(self, user, roles):
        if self.ROLE_LEAD_PROGRAMMER in roles and self.status == self.STATUS_CODE_REVIEW:
            return True
        if self.ROLE_TESTER in roles and self.status == self.STATUS_TESTING:
            return True
        if self.ROLE_MANAGER in roles and self.status in (
            self.STATUS_PERFORMER_REJECTED,
            self.STATUS_WENT_TO_TESTING,
            self.STATUS_TESTER_REJECTED,
            self.STATUS_WAIT_TESTING,
            self.STATUS_TESTING,
            self.STATUS_TESTER_ACCEPTED,

        ):
            return True

    def has_action_reject_perform(self, user, roles):
        if self.ROLE_PERFORMER in roles \
        and self.status in (self.STATUS_WENT_TO_PERFORMER, self.STATUS_PERFORMANCE):
            return True

    def has_action_add_to_performance_queue(self, user, roles):
        if self.ROLE_PERFORMER in roles and self.status == self.STATUS_WENT_TO_PERFORMER:
            return True

    def has_action_start_performance(self, user, roles):
        if self.ROLE_PERFORMER in roles \
        and self.status in (
                self.STATUS_WENT_TO_PERFORMER,
                self.STATUS_WAIT_PERFORMANCE,
                self.STATUS_PERFORMANCE_PAUSE,
        ):
            return True

    def has_action_pause_performance(self, user, roles):
        if self.ROLE_PERFORMER in roles \
        and self.status in (
                self.STATUS_PERFORMANCE,
        ):
            return True

    def has_action_mark_as_performed(self, user, roles):
        if self.ROLE_PERFORMER in roles and self.status == self.STATUS_PERFORMANCE:
            return True

    def has_action_send_to_lead_programmer(self, user, roles):
        if self.lead_programmer:
            if self.ROLE_PERFORMER in roles and self.status == self.STATUS_PERFORMANCE:
                return True

    def has_action_add_to_code_review_queue(self, user, roles):
        if self.ROLE_LEAD_PROGRAMMER in roles and self.status == self.STATUS_WENT_TO_LEAD_PROGRAMMER:
            return True

    def has_action_start_code_review(self, user, roles):
        if self.ROLE_LEAD_PROGRAMMER in roles \
        and self.status in (self.STATUS_WENT_TO_LEAD_PROGRAMMER, self.STATUS_WAIT_CODE_REVIEW):
            return True

    def has_action_send_to_testing(self, user, roles):
        if self.lead_programmer:
            if self.ROLE_LEAD_PROGRAMMER in roles and self.status == self.STATUS_CODE_REVIEW:
                return True
        elif self.tester:
            if self.ROLE_PERFORMER in roles and self.status == self.STATUS_PERFORMED:
                return True

    def has_action_reject_test(self, user, roles):
        if self.ROLE_TESTER in roles and self.status == self.STATUS_TESTING:
            return True

    def has_action_add_to_testing_queue(self, user, roles):
        if self.ROLE_TESTER in roles and self.status == self.STATUS_WENT_TO_TESTING:
            return True

    def has_action_start_testing(self, user, roles):
        if self.ROLE_TESTER in roles and self.status in (self.STATUS_WENT_TO_TESTING, self.STATUS_WAIT_TESTING):
            return True

    def has_action_accept_work_by_tester(self, user, roles):
        if self.ROLE_TESTER in roles and self.status == self.STATUS_TESTING:
            return True

    def has_action_send_to_client(self, user, roles):
        if self.ROLE_MANAGER in roles and self.client:
            if self.tester:
                if self.status == self.STATUS_TESTER_ACCEPTED:
                    return True
            elif self.lead_programmer:
                if self.status == self.STATUS_LEAD_PROGRAMMER_ACCEPTED:
                    return True
            else:
                if self.status == self.STATUS_PERFORMED:
                    return True

    def has_action_add_to_client_checking_queue(self, user, roles):
        if self.ROLE_CLIENT in roles and self.status == self.STATUS_WENT_TO_CLIENT:
            return True

    def has_action_start_client_checking(self, user, roles):
        if self.ROLE_CLIENT in roles and self.status in (self.STATUS_WAIT_CLIENT_CHECKING, self.STATUS_WENT_TO_CLIENT):
            return True

    def has_action_send_to_rework(self, user, roles):
        if self.ROLE_CLIENT in roles and self.status == self.STATUS_CLIENT_CHECKING:
            return True

    def has_action_accept_work_by_client(self, user, roles):
        if self.ROLE_CLIENT in roles and self.status == self.STATUS_CLIENT_CHECKING:
            return True

    def has_action_close_task(self, user, roles):
        if self.manager:
            if self.ROLE_MANAGER in roles:
                return True
        else:
            if self.ROLE_AUTHOR in roles:
                return True

    def run_action(self, action, user):
        """
        Выполняет указанное действие над объектом модели.
        """
        method_name = 'action_{0}'.format(action)
        method = getattr(self, method_name, None)
        if callable(method):
            return method(user)

    def action_send_to_performer(self, user):
        self.status = self.STATUS_WENT_TO_PERFORMER
        self.save()

    def action_reject_perform(self, user):
        self.status = self.STATUS_PERFORMER_REJECTED
        self.save()

    def action_add_to_performance_queue(self, user):
        self.status = self.STATUS_WAIT_PERFORMANCE
        self.save()

    def action_start_performance(self, user):
        self.status = self.STATUS_PERFORMANCE
        self.save()

    def action_pause_performance(self, user):
        self.status = self.STATUS_PERFORMANCE_PAUSE
        self.save()

    def action_mark_as_performed(self, user):
        """
        Помечает задачу как выполненную исполнителем.
        """
        if self.lead_programmer:
            self.status = self.STATUS_WENT_TO_LEAD_PROGRAMMER
        elif self.tester:
            self.status = self.STATUS_WENT_TO_TESTING
        else:
            self.status = self.STATUS_PERFORMED
        self.save()

    def action_add_to_code_review_queue(self, user):
        self.status = self.STATUS_WAIT_CODE_REVIEW
        self.save()

    def action_start_code_review(self, user):
        self.status = self.STATUS_CODE_REVIEW
        self.save()

    def action_send_to_testing(self, user):
        self.status = self.STATUS_WENT_TO_TESTING
        self.save()

    def action_reject_test(self, user):
        self.status = self.STATUS_TESTER_REJECTED
        self.save()

    def action_add_to_testing_queue(self, user):
        self.status = self.STATUS_WAIT_TESTING
        self.save()

    def action_start_testing(self, user):
        self.status = self.STATUS_TESTING
        self.save()

    def action_accept_work_by_tester(self, user):
        self.status = self.STATUS_TESTER_ACCEPTED
        self.save()

    def action_send_to_client(self, user):
        self.status = self.STATUS_WENT_TO_CLIENT
        self.save()

    def action_add_to_client_checking_queue(self, user):
        self.status = self.STATUS_WAIT_CLIENT_CHECKING
        self.save()

    def action_start_client_checking(self, user):
        self.status = self.STATUS_CLIENT_CHECKING
        self.save()

    def action_send_to_rework(self, user):
        self.status = self.STATUS_CLIENT_REJECTED
        self.save()

    def action_accept_work_by_client(self, user):
        self.status = self.STATUS_CLIENT_ACCEPTED
        self.save()

    def action_close_task(self, user):
        self.status = self.STATUS_CLOSED
        self.save()


class Task(EntityBaseFields, TitleField, DescField,
           TaskFieldsAccessTypeMixin, TaskActionsMixin):
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

    # использую константы для всех статусов, чтобы свести к минимуму ошибки
    # опечаток использования статусов
    STATUS_WENT_TO_PERFORMER  = 11
    STATUS_PERFORMER_REJECTED = 12
    STATUS_WAIT_PERFORMANCE   = 13
    STATUS_PERFORMANCE        = 14
    STATUS_PERFORMANCE_PAUSE  = 15
    STATUS_PERFORMED          = 16

    STATUS_WENT_TO_LEAD_PROGRAMMER  = 21
    STATUS_WAIT_CODE_REVIEW         = 22
    STATUS_CODE_REVIEW              = 23
    STATUS_LEAD_PROGRAMMER_ACCEPTED = 24

    STATUS_WENT_TO_TESTING = 31
    STATUS_TESTER_REJECTED = 32
    STATUS_WAIT_TESTING    = 33
    STATUS_TESTING         = 34
    STATUS_TESTER_ACCEPTED = 35

    STATUS_WENT_TO_CLIENT       = 41
    STATUS_WAIT_CLIENT_CHECKING = 42
    STATUS_CLIENT_CHECKING      = 43
    STATUS_CLIENT_ACCEPTED      = 44
    STATUS_CLIENT_REJECTED      = 45
    STATUS_CLOSED               = 46

    STATUSES = {
        STATUS_WENT_TO_PERFORMER  : u'Отправлена исполнителю',
        STATUS_PERFORMER_REJECTED : u'Отказ выполнять',
        STATUS_WAIT_PERFORMANCE   : u'Ожидает выполнения',
        STATUS_PERFORMANCE        : u'Выполнение',
        STATUS_PERFORMANCE_PAUSE  : u'Пауза',
        STATUS_PERFORMED          : u'Решено',

        STATUS_WENT_TO_LEAD_PROGRAMMER : u'Отправлена тимлиду',
        STATUS_WAIT_CODE_REVIEW        : u'Ожидает проверки кода',
        STATUS_CODE_REVIEW             : u'Проверка кода',

        STATUS_WENT_TO_TESTING : u'Отправлена на тестирование',
        STATUS_TESTER_REJECTED : u'Отказ тестировать',
        STATUS_WAIT_TESTING    : u'Ожидает тестирования',
        STATUS_TESTING         : u'Тестирование',
        STATUS_TESTER_ACCEPTED : u'Успешно протестирована',

        STATUS_WENT_TO_CLIENT       : u'Отправлена заказчику',
        STATUS_WAIT_CLIENT_CHECKING : u'Ожидает проверки заказчиком',
        STATUS_CLIENT_CHECKING      : u'Проверка заказчиком',
        STATUS_CLIENT_REJECTED      : u'Не принята заказчиком',
        STATUS_CLIENT_ACCEPTED      : u'Принята заказчиком',
        STATUS_CLOSED               : u'Завершена',
    }

    # роли пользователя в данной задаче
    ROLE_SUPERUSER       = 'superuser'
    ROLE_AUTHOR          = 'author'
    ROLE_PERFORMER       = 'performer'
    ROLE_LEAD_PROGRAMMER = 'lead_programmer'
    ROLE_TESTER          = 'tester'
    ROLE_MANAGER         = 'manager'
    ROLE_CLIENT          = 'client'

    priority   = models.IntegerField(choices = PRIORITY_CHOICES.items(), verbose_name = u'Срочность', default = 0)
    importance = models.IntegerField(choices = IMPORTANCE_CHOICES.items(), verbose_name = u'Важность', default = 0)
    author     = models.ForeignKey('account.Account', verbose_name = u'Автор', related_name = 'task_author')

    status = models.IntegerField(max_length = 30, choices = STATUSES.items(), verbose_name = u'Статус', default = STATUS_WENT_TO_PERFORMER)

    performer       = models.ForeignKey('account.Account', verbose_name = u'Исполнитель', related_name = 'task_performer', blank = True, null = True)
    lead_programmer = models.ForeignKey('account.Account', verbose_name = u'Ведущий разработчик', related_name = 'task_lead_programmer', blank = True, null = True)
    tester          = models.ForeignKey('account.Account', verbose_name = u'Тестировщик', related_name = 'task_tester', blank = True, null = True)
    manager         = models.ForeignKey('account.Account', verbose_name = u'Менеджер', related_name = 'task_manager', blank = True, null = True)
    client          = models.ForeignKey('account.Account', verbose_name = u'Клиент', related_name = 'task_client', blank = True, null = True)

    project    = models.ForeignKey('project.Project', verbose_name = u'Проект', related_name = 'task_project', blank = True, null = True)

    # objects = models.Manager()

    class Meta():
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def get_user_roles(self, user):
        """
        Возвращает список ролей указанного пользователя в данной задаче
        """
        roles = []
        if user.is_superuser:
            roles.append(self.ROLE_SUPERUSER)

        if user.pk == getattr(self.performer, 'pk', None):
            roles.append(self.ROLE_PERFORMER)

        if user.pk == getattr(self.lead_programmer, 'pk', None):
            roles.append(self.ROLE_LEAD_PROGRAMMER)

        if user.pk == getattr(self.tester, 'pk', None):
            roles.append(self.ROLE_TESTER)

        if user.pk == getattr(self.manager, 'pk', None):
            roles.append(self.ROLE_MANAGER)

        if user.pk == getattr(self.client, 'pk', None):
            roles.append(self.ROLE_CLIENT)

        return set(roles)

    def get_field_available_choices(self, user, field_name):
        """
        Возвращает словарь допустимых значений
        указанному пользователю для указанного поля.
        """
        method_name = 'get_{0}_field_available_choices'.format(field_name)
        method = getattr(self, method_name)
        if callable(method):
            return method(user)

    def get_members(self, only_ids=False):
        """
        Возвращает всех пользователей, которые учавствуют в работе над задачей.
        """
        members = []
        if self.performer:
            members.append(self.performer)
        if self.lead_programmer:
            members.append(self.lead_programmer)
        if self.tester:
            members.append(self.tester)
        if self.manager:
            members.append(self.manager)
        if self.client:
            members.append(self.client)

        if only_ids:
            return [u.id for u in members]
        else:
            return members


@receiver(post_save, sender=Task)
def task_post_save(sender, instance, *args, **kwargs):
    collections_fabric = TaskCollectionsFabric(instance)
    # добавляем задачу в коллекции, которым подходит данная задача по свойствам
    for c in collections_fabric.get_appropriate_collections():
        c.add_item(instance.pk)
    # исключаем задачу из коллекций, которым данная задача не подходит по свойствам
    for c in collections_fabric.get_inappropriate_collections():
        c.delete_item(instance.pk)
