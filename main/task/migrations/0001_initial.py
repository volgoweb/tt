# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import main.helper.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('active', models.BooleanField(default=True, help_text='\u0415\u0441\u043b\u0438 \u043d\u0435 \u0430\u043a\u0442\u0438\u0432\u043d\u043e, \u0442\u043e \u043d\u0435 \u0431\u0443\u0434\u0435\u0442 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c\u0441\u044f \u043d\u0430 \u0441\u0430\u0439\u0442\u0435.', verbose_name='\u0410\u043a\u0442\u0438\u0432\u043d\u043e')),
                ('title', models.CharField(max_length=254, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True)),
                ('desc', models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('priority', models.IntegerField(default=0, verbose_name='\u041f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442', choices=[(0, 0), (1, 1), (2, 2), (-1, -1), (-2, -2)])),
                ('status', models.CharField(default=b'new', max_length=20, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441', choices=[(b'in_work', 'In work'), (b'new', 'New'), (b'ready', 'Ready')])),
                ('author', models.ForeignKey(related_name=b'task_author', verbose_name='\u0410\u0432\u0442\u043e\u0440', to=settings.AUTH_USER_MODEL)),
                ('client', models.ForeignKey(related_name=b'task_client', verbose_name='\u041a\u043b\u0438\u0435\u043d\u0442', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('developer', models.ForeignKey(related_name=b'task_developer', verbose_name='\u0420\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a', to=settings.AUTH_USER_MODEL)),
                ('manager', models.ForeignKey(related_name=b'task_manager', verbose_name='\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('project', models.ForeignKey(related_name=b'task_project', verbose_name='\u041f\u0440\u043e\u0435\u043a\u0442', blank=True, to='project.Project', null=True)),
                ('tester', models.ForeignKey(related_name=b'task_tester', verbose_name='\u0422\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0449\u0438\u043a', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
            bases=(models.Model, main.helper.models.FieldsLabelsMixin),
        ),
    ]
