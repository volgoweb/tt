# -*- coding: utf-8 -*-
from main.helper.collection.collections import get_collection_class


class TaskCollectionsFabric(object):
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
        # Коллекция "ожидают реакции"
        collect_name = 'wait_reaction:uid_{0}'.format(self.task.performer.pk)
        collection = collection_class(name=collect_name)

        if self.task.status in (self.task.STATUS_WENT_TO_PERFORMER,):
            self.appropriate_collections.append(collection)
        else:
            self.inappropriate_collections.append(collection)

        # Коллекция "мои в работе"
        collect_name = 'my_in_work:uid_{0}'.format(self.task.performer.pk)
        collection = collection_class(name=collect_name)
        if self.task.status in (self.task.STATUS_PERFORMANCE, self.task.STATUS_PERFORMANCE_PAUSE):
            self.appropriate_collections.append(collection)
        else:
            self.inappropriate_collections.append(collection)

        # Коллекция "в очереди"
        collect_name = 'in_queue:uid_{0}'.format(self.task.performer.pk)
        collection = collection_class(name=collect_name)
        if self.task.status in (self.task.STATUS_WAIT_PERFORMANCE,):
            self.appropriate_collections.append(collection)
        else:
            self.inappropriate_collections.append(collection)

        # Коллекция "все"
        collect_name = 'all:uid_{0}'.format(self.task.performer.pk)
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
