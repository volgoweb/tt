# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20141006_1340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='developer',
        ),
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
        migrations.AddField(
            model_name='task',
            name='client_work_status',
            field=models.CharField(default=b'new', max_length=30, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441 \u0440\u0430\u0431\u043e\u0442\u044b \u043a\u043b\u0438\u0435\u043d\u0442\u0430', choices=[(b'in_work', '\u0412 \u0440\u0430\u0431\u043e\u0442\u0435'), (b'new', '\u041d\u0435 \u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u043d\u043e'), (b'ready', '\u0420\u0435\u0448\u0435\u043d\u0430'), (b'in_queue', '\u0412 \u043e\u0447\u0435\u0440\u0435\u0434\u0438'), (b'rejected', '\u041e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0430')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='manager_work_status',
            field=models.CharField(default=b'new', max_length=30, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441 \u0440\u0430\u0431\u043e\u0442\u044b \u043c\u0435\u043d\u0435\u0434\u0436\u0435\u0440\u0430', choices=[(b'in_work', '\u0412 \u0440\u0430\u0431\u043e\u0442\u0435'), (b'new', '\u041d\u0435 \u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u043d\u043e'), (b'ready', '\u0420\u0435\u0448\u0435\u043d\u0430'), (b'in_queue', '\u0412 \u043e\u0447\u0435\u0440\u0435\u0434\u0438'), (b'rejected', '\u041e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0430')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='performer_work_status',
            field=models.CharField(default=b'new', max_length=30, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441 \u0440\u0430\u0431\u043e\u0442\u044b \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f', choices=[(b'in_work', '\u0412 \u0440\u0430\u0431\u043e\u0442\u0435'), (b'new', '\u041d\u0435 \u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u043d\u043e'), (b'ready', '\u0420\u0435\u0448\u0435\u043d\u0430'), (b'in_queue', '\u0412 \u043e\u0447\u0435\u0440\u0435\u0434\u0438'), (b'rejected', '\u041e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0430')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='tester_work_status',
            field=models.CharField(default=b'new', max_length=30, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441 \u0440\u0430\u0431\u043e\u0442\u044b \u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0449\u0438\u043a\u0430', choices=[(b'in_work', '\u0412 \u0440\u0430\u0431\u043e\u0442\u0435'), (b'new', '\u041d\u0435 \u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u043d\u043e'), (b'ready', '\u0420\u0435\u0448\u0435\u043d\u0430'), (b'in_queue', '\u0412 \u043e\u0447\u0435\u0440\u0435\u0434\u0438'), (b'rejected', '\u041e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0430')]),
            preserve_default=True,
        ),
    ]
