# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='importance',
            field=models.IntegerField(default=0, verbose_name='\u0412\u0430\u0436\u043d\u043e\u0441\u0442\u044c', choices=[(0, '\u041e\u0431\u044b\u0447\u043d\u043e'), (1, '\u0412\u0430\u0436\u043d\u043e'), (2, '\u041e\u0447\u0435\u043d\u044c \u0432\u0430\u0436\u043d\u043e'), (-1, '\u041d\u0435 \u0432\u0430\u0436\u043d\u043e'), (-2, '\u0421\u043e\u0432\u0441\u0435\u043c \u043d\u0435 \u0432\u0430\u0436\u043d\u043e')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='performer',
            field=models.ForeignKey(related_name=b'task_performer', verbose_name='\u0418\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='developer',
            field=models.ForeignKey(related_name=b'task_developer', verbose_name='\u0420\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.IntegerField(default=0, verbose_name='\u0421\u0440\u043e\u0447\u043d\u043e\u0441\u0442\u044c', choices=[(0, '\u041e\u0431\u044b\u0447\u043d\u043e'), (1, '\u0421\u0440\u043e\u0447\u043d\u043e'), (2, '\u041e\u0447\u0435\u043d\u044c \u0441\u0440\u043e\u0447\u043d\u043e'), (-1, '\u041d\u0435 \u0441\u0440\u043e\u0447\u043d\u043e'), (-2, '\u0421\u043e\u0432\u0441\u0435\u043c \u043d\u0435 \u0441\u0440\u043e\u0447\u043d\u043e')]),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(default=b'new', max_length=20, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441', choices=[(b'ready', '\u0420\u0435\u0448\u0435\u043d\u0430'), (b'accepted_by_manager', '\u041f\u0440\u0438\u043d\u044f\u0442\u0430 \u043c\u0435\u043d\u0435\u0434\u0436\u0435\u0440\u043e\u043c'), (b'closed', '\u0417\u0430\u043a\u0440\u044b\u0442\u0430'), (b'tested', '\u041f\u0440\u043e\u0432\u0435\u0440\u0435\u043d\u0430 \u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0449\u0438\u043a\u043e\u043c'), (b'in_work', '\u0412 \u0440\u0430\u0431\u043e\u0442\u0435'), (b'new', '\u041d\u043e\u0432\u0430\u044f'), (b'accepted_by_client', '\u041f\u0440\u0438\u043d\u044f\u0442\u0430 \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u043c'), (b'in_queue', '\u0412 \u043e\u0447\u0435\u0440\u0435\u0434\u0438'), (b'rejected', '\u041e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0430')]),
        ),
    ]
