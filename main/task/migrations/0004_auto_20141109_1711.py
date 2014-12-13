# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0003_auto_20141107_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='client_work_status',
        ),
        migrations.RemoveField(
            model_name='task',
            name='manager_work_status',
        ),
        migrations.RemoveField(
            model_name='task',
            name='performer_work_status',
        ),
        migrations.RemoveField(
            model_name='task',
            name='tester_work_status',
        ),
        migrations.AddField(
            model_name='task',
            name='lead_programmer',
            field=models.ForeignKey(related_name=b'task_lead_programmer', verbose_name='\u0412\u0435\u0434\u0443\u0449\u0438\u0439 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(default=b'STATUS_WENT_TO_PERFORMER', max_length=30, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441', choices=[(b'STATUS_WAIT_PERFORMANCE', '\u041e\u0436\u0438\u0434\u0430\u0435\u0442 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f'), (b'STATUS_CLIENT_REJECTED', '\u041d\u0435 \u043f\u0440\u0438\u043d\u044f\u0442\u0430 \u0437\u0430\u043a\u0430\u0437\u0447\u0438\u043a\u043e\u043c'), (b'STATUS_CLIENT_ACCEPTED', '\u041f\u0440\u0438\u043d\u044f\u0442\u0430 \u0437\u0430\u043a\u0430\u0437\u0447\u0438\u043a\u043e\u043c'), (b'STATUS_PERFORMER_REJECTED', '\u041e\u0442\u043a\u0430\u0437 \u0432\u044b\u043f\u043e\u043b\u043d\u044f\u0442\u044c'), (b'STATUS_TESTER_REJECTED', '\u041e\u0442\u043a\u0430\u0437 \u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c'), (b'STATUS_WAIT_CODE_REVIEW', '\u041e\u0436\u0438\u0434\u0430\u0435\u0442 \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438 \u043a\u043e\u0434\u0430'), (b'STATUS_WENT_TO_LEAD_PROGRAMMER', '\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0430 \u0442\u0438\u043c\u043b\u0438\u0434\u0443'), (b'STATUS_WAIT_CLIENT_CHECKING', '\u041e\u0436\u0438\u0434\u0430\u0435\u0442 \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438 \u0437\u0430\u043a\u0430\u0437\u0447\u0438\u043a\u043e\u043c'), (b'STATUS_CLIENT_CHECKING', '\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430 \u0437\u0430\u043a\u0430\u0437\u0447\u0438\u043a\u043e\u043c'), (b'STATUS_CLOSED', '\u0417\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0430'), (b'STATUS_WAIT_TESTING', '\u041e\u0436\u0438\u0434\u0430\u0435\u0442 \u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f'), (b'STATUS_CODE_REVIEW', '\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430 \u043a\u043e\u0434\u0430'), (b'STATUS_WENT_TO_CLIENT', '\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0430 \u0437\u0430\u043a\u0430\u0437\u0447\u0438\u043a\u0443'), (b'STATUS_WENT_TO_TESTING', '\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0430 \u043d\u0430 \u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435'), (b'STATUS_TESTER_ACCEPTED', '\u0423\u0441\u043f\u0435\u0448\u043d\u043e \u043f\u0440\u043e\u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0430'), (b'STATUS_TESTING', '\u0422\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435'), (b'STATUS_PERFORMANCE', '\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435'), (b'STATUS_WENT_TO_PERFORMER', '\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0430 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044e')]),
            preserve_default=True,
        ),
    ]
