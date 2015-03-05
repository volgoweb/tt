# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0001_initial'),
        ('project', '0002_auto_20141006_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='last_release',
            field=models.ForeignKey(related_name=b'project_last_release', verbose_name='\u041f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0438\u0439 \u0440\u0435\u043b\u0438\u0437', blank=True, to='release.Release', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='next_release',
            field=models.ForeignKey(related_name=b'project_next_release', verbose_name='\u0421\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u0439 \u0440\u0435\u043b\u0438\u0437', blank=True, to='release.Release', null=True),
            preserve_default=True,
        ),
    ]
