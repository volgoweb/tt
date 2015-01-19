# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.conf import settings


class CollectionConfig(AppConfig):
    name = 'Collection'
    verbose_name = u'Коллекция'

    # Возможные значения для места хранения коллекций (свойство "backend")
    BACKEND_REDIS = 'redis'
    BACKEND_ORM = 'orm'
    BACKEND_CACHE = 'cache'
    # Место хранения коллекций объектов
    BACKEND = getattr(settings, 'COLLECTION_BACKEND_REDIS', None) or BACKEND_REDIS

    # подключение к БД redis
    REDIS_HOST = getattr(settings, 'COLLECTION_REDIS_HOST', None) or 'localhost'
    REDIS_PORT = getattr(settings, 'COLLECTION_REDIS_PORT', None) or '6379'
    REDIS_DB = getattr(settings, 'COLLECTION_REDIS_DB', None) or '0'

    # количество элементов коллекции на одной странице
    PER_PAGE = 10
