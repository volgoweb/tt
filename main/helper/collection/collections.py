# -*- coding: utf-8 -*-
import redis
import math
from .conf import CollectionConfig
from abc import ABCMeta, abstractmethod


class BaseCollection(object):
    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name')
        self.per_page = kwargs.get('per_page', CollectionConfig.PER_PAGE)

    @abstractmethod
    def clear(self):
        """
        Очистка коллекции.
        """
        pass

    @abstractmethod
    def add_item(self, item):
        """
        Добавляет объект в коллекцию.

        Keywords arguments:
            item -- int or string
        """
        self.backend.add_item(item)

    @abstractmethod
    def delete_item(self, item):
        """
        Удаляет объект из коллекции.

        Keywords arguments:
            item -- int or string
        """
        pass

    @abstractmethod
    def contains_item(self, item):
        """
        Проверяет, содержит ли коллекция указанный объект.

        Keywords arguments:
            item -- int or string
        """
        pass

    @abstractmethod
    def get_count_items(self):
        """
        Возвращает общее количество объектов, содержащихся в коллекции.
        """
        pass

    def get_count_pages(self):
        """
        Возвращает количество страниц.
        """
        count_items = self.get_count_items()
        return math.ceil(float(count_items) / self.per_page)

    @abstractmethod
    def get_items_paginated(self, num_page=1):
        """
        Возвращает набор объектов для указанного номера страницы.

        Keywords arguments:
            num_page -- int - номер страницы (default 1)
        """
        pass

    @abstractmethod
    def get_items(self):
        """
        Возвращает содержимое коллекции.
        """
        pass


class RedisCollection(BaseCollection):
    def __init__(self, *args, **kwargs):
        super(RedisCollection, self).__init__(*args, **kwargs)
        self.redis = redis.StrictRedis(host=CollectionConfig.REDIS_HOST, port=CollectionConfig.REDIS_PORT, db=CollectionConfig.REDIS_DB)

    def add_item(self, item):
        self.redis.sadd(self.name, item)

    def add_items(self, items):
        for item in items:
            self.redis.sadd(self.name, item)

    def delete_item(self, item):
        self.redis.srem(self.name, item)

    def get_items(self):
        items = self.redis.smembers(self.name)
        return items

    def get_items_paginated(self, num_page=1):
        items = self.get_items()
        if page < 1:
            raise 'Number page not valid.'
        index_from = self.per_page * (page - 1)
        index_to = index_from + self.per_page
        return items[index_from, index_to]

    def clear(self):
        self.redis.delete(self.name)


def get_collection_class():
    if CollectionConfig.BACKEND == CollectionConfig.BACKEND_REDIS:
        return RedisCollection
    raise 'Invalid backend in settings'
