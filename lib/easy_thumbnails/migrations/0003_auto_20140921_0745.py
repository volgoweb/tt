# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easy_thumbnails', '0002_thumbnaildimensions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thumbnail',
            name='source',
            field=models.ForeignKey(related_name=b'thumbnails', to='easy_thumbnails.Source'),
        ),
        migrations.AlterField(
            model_name='thumbnaildimensions',
            name='thumbnail',
            field=models.OneToOneField(related_name=b'dimensions', to='easy_thumbnails.Thumbnail'),
        ),
    ]
