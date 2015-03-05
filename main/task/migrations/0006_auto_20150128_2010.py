# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0002_auto_20150124_1956'),
        ('specification', '0001_initial'),
        ('task', '0005_auto_20150107_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='release',
            field=models.ForeignKey(related_name=b'task_release', verbose_name='\u0420\u0435\u043b\u0438\u0437', blank=True, to='release.Release', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='specification',
            field=models.ForeignKey(related_name=b'task_specification', verbose_name='\u0413\u043b\u0430\u0432\u0430 \u0422\u0417', blank=True, to='specification.Specification', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(default=11, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441', choices=[(32, '\u041e\u0442\u043a\u0430\u0437 \u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c'), (33, '\u041e\u0436\u0438\u0434\u0430\u0435\u0442 \u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f'), (34, '\u0422\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435'), (35, '\u0423\u0441\u043f\u0435\u0448\u043d\u043e \u043f\u0440\u043e\u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0430'), (41, '\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0430 \u0437\u0430\u043a\u0430\u0437\u0447\u0438\u043a\u0443'), (42, '\u041e\u0436\u0438\u0434\u0430\u0435\u0442 \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438 \u0437\u0430\u043a\u0430\u0437\u0447\u0438\u043a\u043e\u043c'), (11, '\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0430 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044e'), (12, '\u041e\u0442\u043a\u0430\u0437 \u0432\u044b\u043f\u043e\u043b\u043d\u044f\u0442\u044c'), (13, '\u041e\u0436\u0438\u0434\u0430\u0435\u0442 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f'), (14, '\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435'), (15, '\u041f\u0430\u0443\u0437\u0430'), (16, '\u0420\u0435\u0448\u0435\u043d\u043e'), (43, '\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430 \u0437\u0430\u043a\u0430\u0437\u0447\u0438\u043a\u043e\u043c'), (21, '\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0430 \u0442\u0438\u043c\u043b\u0438\u0434\u0443'), (22, '\u041e\u0436\u0438\u0434\u0430\u0435\u0442 \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438 \u043a\u043e\u0434\u0430'), (23, '\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430 \u043a\u043e\u0434\u0430'), (45, '\u041d\u0435 \u043f\u0440\u0438\u043d\u044f\u0442\u0430 \u0437\u0430\u043a\u0430\u0437\u0447\u0438\u043a\u043e\u043c'), (46, '\u0417\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0430'), (44, '\u041f\u0440\u0438\u043d\u044f\u0442\u0430 \u0437\u0430\u043a\u0430\u0437\u0447\u0438\u043a\u043e\u043c'), (31, '\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0430 \u043d\u0430 \u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435')]),
        ),
        migrations.AlterField(
            model_name='task',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f'),
        ),
    ]
