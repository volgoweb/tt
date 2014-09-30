# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name='\u0430\u0434\u0440\u0435\u0441 \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u043e\u0439 \u043f\u043e\u0447\u0442\u044b')),
                ('first_name', models.CharField(max_length=30, verbose_name='\u0438\u043c\u044f')),
                ('middle_name', models.CharField(max_length=30, verbose_name='middle name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='\u0444\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('job', models.CharField(max_length=50, verbose_name='job')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
