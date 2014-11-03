# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='clients',
            field=models.ManyToManyField(related_name=b'task_clients', null=True, verbose_name='\u041a\u043b\u0438\u0435\u043d\u0442\u044b', to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='designers',
            field=models.ManyToManyField(related_name=b'task_designers', null=True, verbose_name='\u0414\u0438\u0437\u0430\u0439\u043d\u0435\u0440\u044b', to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='managers',
            field=models.ManyToManyField(related_name=b'task_managers', null=True, verbose_name='\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440\u044b', to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(related_name=b'task_memebers', null=True, verbose_name='\u0423\u0447\u0430\u0441\u0442\u043d\u0438\u043a\u0438', to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='testers',
            field=models.ManyToManyField(related_name=b'task_testers', null=True, verbose_name='\u0422\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0449\u0438\u043a\u0438', to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
    ]
