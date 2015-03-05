# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20150108_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u0441\u043e\u0437\u0434\u0430\u043d'),
        ),
    ]
