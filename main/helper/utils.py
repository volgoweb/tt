# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def add_pagingation(models, page, per_page = 10):
    paginator = Paginator(models, per_page)
    try:
        models = paginator.page(page)
    except PageNotAnInteger:
        models = paginator.page(1)
    except EmptyPage:
        models = paginator.page(paginator.num_pages)
    return models
