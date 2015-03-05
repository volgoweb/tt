# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='date',
            field=models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430', blank=True),
        ),
    ]
