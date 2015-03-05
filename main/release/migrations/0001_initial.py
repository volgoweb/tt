# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20141006_1340'),
    ]

    operations = [
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=254, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True)),
                ('desc', models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('date', models.DateTimeField(null=True, verbose_name='\u0414\u0430\u0442\u0430', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f')),
                ('status', models.IntegerField(default=10, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441', choices=[(70, '\u0413\u043e\u0442\u043e\u0432 \u0438 \u0432\u044b\u043b\u043e\u0436\u0435\u043d \u043d\u0430 \u043f\u0440\u043e\u0434\u0430\u043a\u0448\u0435\u043d'), (40, '\u0422\u0435\u0441\u0442\u0438\u0440\u0443\u0435\u0442\u0441\u044f'), (10, '\u0412 \u043e\u0447\u0435\u0440\u0435\u0434\u0438'), (50, '\u0414\u043e\u0440\u0430\u0431\u043e\u0442\u043a\u0430'), (20, '\u0412 \u0440\u0430\u0431\u043e\u0442\u0435'), (60, '\u0413\u043e\u0442\u043e\u0432 \u043a \u0434\u0435\u043f\u043b\u043e\u044e'), (30, '\u0413\u043e\u0442\u043e\u0432')])),
                ('project', models.ForeignKey(related_name=b'release_project', to='project.Project')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
