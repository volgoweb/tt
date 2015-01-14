# -*- coding: utf-8 -*-
from main.helper.collection.collections import get_collection_class


class TaskCollectionsFabric(object):
    # шаблоны названий коллекций, содержащих id задач 
    # для соответствующего списка определенного пользователя.
    # Вместо {0} будет подставляться id пользователя.
    PATTERN_WAIT_REACTION = 'wait_reaction:uid_{0}'
    PATTERN_MY_IN_WORK = 'my_in_work:uid_{0}'
    PATTERN_IN_QUEUE = 'in_queue:uid_{0}'
    PATTERN_ALL = 'all:uid_{0}'
    PATTERNS_OF_LIST_TASKS_COLLECTIONS_NAMES = [
        PATTERN_WAIT_REACTION,
        PATTERN_MY_IN_WORK,
        PATTERN_IN_QUEUE,
        PATTERN_ALL,
    ]

    def __init__(self, task):
        self.task = task
        self.define_collections()

    def define_collections(self):
        """
        Формируем списки подходящих и неподходящих для задачи коллекций.
        """
        self.appropriate_collections = []
        self.inappropriate_collections = []
        collection_class = get_collection_class()

        #
        # Коллекции для исполнителя:
        #
        mapping = {
            'performer': {
                self.PATTERN_WAIT_REACTION: (self.task.STATUS_WENT_TO_PERFORMER,),
                self.PATTERN_MY_IN_WORK: (self.task.STATUS_PERFORMANCE, self.task.STATUS_PERFORMANCE_PAUSE),
                self.PATTERN_IN_QUEUE: (self.task.STATUS_WAIT_PERFORMANCE,),
            },
            'lead_programmer': {
                self.PATTERN_WAIT_REACTION: (self.task.STATUS_WENT_TO_LEAD_PROGRAMMER,),
                self.PATTERN_MY_IN_WORK: (self.task.STATUS_CODE_REVIEW,),
                self.PATTERN_IN_QUEUE: (self.task.STATUS_WAIT_CODE_REVIEW,),
            },
            'tester': {
                self.PATTERN_WAIT_REACTION: (self.task.STATUS_WENT_TO_TESTING,),
                self.PATTERN_MY_IN_WORK: (self.task.STATUS_TESTING,),
                self.PATTERN_IN_QUEUE: (self.task.STATUS_WAIT_TESTING,),
            },
            'manager': {
                self.PATTERN_WAIT_REACTION: (
                    self.task.STATUS_CLIENT_REJECTED,
                    self.task.STATUS_CLIENT_ACCEPTED,
                ),
                self.PATTERN_MY_IN_WORK: (
                    self.task.STATUS_WENT_TO_TESTING,
                    self.task.STATUS_WAIT_TESTING,
                    self.task.STATUS_TESTING,
                    self.task.STATUS_TESTER_ACCEPTED,
                ),
                # self.PATTERN_IN_QUEUE: (self.task.STATUS_WAIT_TESTING,),
            },
            'client': {
                self.PATTERN_WAIT_REACTION: (self.task.STATUS_WENT_TO_CLIENT,),
                self.PATTERN_MY_IN_WORK: (self.task.STATUS_CLIENT_CHECKING,),
                self.PATTERN_IN_QUEUE: (self.task.STATUS_WAIT_CLIENT_CHECKING,),
            },
        }

        # Определим пользователей, которые до текущего момента имели отношение к задаче,
        # но теперь не имеют и из их списков нужно это задачу убрать
        collect_name = 'task_members:tid_{0}'.format(self.task.pk)
        collection = collection_class(name=collect_name)
        old_members_ids = set(collection.get_items())
        new_members_ids = set(self.task.get_members(only_ids=True))
        removed_members = old_members_ids - new_members_ids
        # Обновляем список пользователей, имеющих отношение к задаче
        collection.clear()
        collection.add_items(new_members_ids)
        for uid in removed_members:
            for pattern in self.PATTERNS_OF_LIST_TASKS_COLLECTIONS_NAMES:
                collect_name = pattern.format(uid)
                collection = collection_class(name=collect_name)
                collection.delete_item(self.task.pk)

        # Проходим по всем коллекциям и расфасовываем коллекции в 
        # подходящие (в которых должна присутствовать данная задача) и
        # неподходящие (из которых нужно удалить данную задачу)
        for member_field_name, collection_conditions in mapping.iteritems():
            member = getattr(self.task, member_field_name, None)
            if not member:
                continue
            for pattern, available_statuses in collection_conditions.iteritems():
                collect_name = pattern.format(getattr(member, 'pk'))
                collection = collection_class(name=collect_name)

                # TODO удаленные задачи надо убирать из списков
                if not self.task.active:
                    self.inappropriate_collections.append(collection)
                elif self.task.status in available_statuses:
                    self.appropriate_collections.append(collection)
                else:
                    self.inappropriate_collections.append(collection)

            # Коллекция "все"
            collect_name = 'all:uid_{0}'.format(getattr(member, 'pk'))
            collection = collection_class(name=collect_name)
            self.appropriate_collections.append(collection)

    def get_appropriate_collections(self):
        """
        Возвращает список коллекций, которые должны содержать указанную задачу.
        """
        return self.appropriate_collections

    def get_inappropriate_collections(self):
        """
        Возвращает список коллекций, которые не должны содержать указанную задачу.
        """
        return self.inappropriate_collections
