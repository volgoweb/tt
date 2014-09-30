# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import main.helper.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('active', models.BooleanField(default=True, help_text='\u0415\u0441\u043b\u0438 \u043d\u0435 \u0430\u043a\u0442\u0438\u0432\u043d\u043e, \u0442\u043e \u043d\u0435 \u0431\u0443\u0434\u0435\u0442 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c\u0441\u044f \u043d\u0430 \u0441\u0430\u0439\u0442\u0435.', verbose_name='\u0410\u043a\u0442\u0438\u0432\u043d\u043e')),
                ('title', models.CharField(max_length=254, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True)),
                ('desc', models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
            bases=(models.Model, main.helper.models.FieldsLabelsMixin),
        ),
    ]
