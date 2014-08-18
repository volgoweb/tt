# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Constance'
        db.create_table('constance_config', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('value', self.gf('picklefield.fields.PickledObjectField')()),
        ))
        db.send_create_signal(u'database', ['Constance'])


    def backwards(self, orm):
        # Deleting model 'Constance'
        db.delete_table('constance_config')


    models = {
        u'database.constance': {
            'Meta': {'object_name': 'Constance', 'db_table': "'constance_config'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'value': ('picklefield.fields.PickledObjectField', [], {})
        }
    }

    complete_apps = ['database']