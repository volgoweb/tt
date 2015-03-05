# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=254, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True)),
                ('desc', models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f')),
                ('status', models.IntegerField(default=1, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441', choices=[(1, '\u041d\u043e\u0432\u0430\u044f'), (46, '\u0421\u0434\u0435\u043b\u0430\u043d\u0430 \u0438 \u0432\u044b\u043b\u043e\u0436\u0435\u043d\u0430 \u043d\u0430 \u043f\u0440\u043e\u0434\u0430\u043a\u0448\u0435\u043d')])),
                ('release', models.ForeignKey(related_name=b'specification_release', verbose_name='\u0420\u0435\u043b\u0438\u0437', to='release.Release', help_text='\u0420\u0435\u043b\u0438\u0437, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u043c \u043f\u043b\u0430\u043d\u0438\u0440\u0443\u0435\u0442\u0441\u044f \u0432\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u043e\u0435 \u0422\u0417')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
