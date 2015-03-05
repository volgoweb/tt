# -*- coding: utf-8 -*-
from __future__ import absolute_import
from celery import Celery, task, shared_task

from .collections import TaskCollectionsFabric

# app = Celery('tasks', broker='amqp://guest@localhost//')

@shared_task
def caching_all_rendered_tasks_items(instance):
    collections_fabric = TaskCollectionsFabric(instance)
    # добавляем задачу в коллекции, которым подходит данная задача по свойствам
    for c in collections_fabric.get_appropriate_collections():
        c.add_item(instance.pk)
    # исключаем задачу из коллекций, которым данная задача не подходит по свойствам
    for c in collections_fabric.get_inappropriate_collections():
        c.delete_item(instance.pk)

    return True
