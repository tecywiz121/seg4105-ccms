# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Assignment.cost'
        db.add_column('hotseat_assignment', 'cost',
                      self.gf('django.db.models.fields.DecimalField')(default=-1, max_digits=10, decimal_places=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Assignment.cost'
        db.delete_column('hotseat_assignment', 'cost')


    models = {
        'hotseat.assignment': {
            'Meta': {'object_name': 'Assignment'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keepalive_last': ('django.db.models.fields.IntegerField', [], {}),
            'keepalive_token': ('django.db.models.fields.CharField', [], {'default': "'YpHV5dVCW2'", 'max_length': '10', 'blank': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'default': "'15906'", 'max_length': '10', 'blank': 'True'}),
            'terminal': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'assignments'", 'to': "orm['hotseat.Terminal']"}),
            'time_remaining': ('django.db.models.fields.IntegerField', [], {})
        },
        'hotseat.terminal': {
            'Meta': {'object_name': 'Terminal'},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'})
        }
    }

    complete_apps = ['hotseat']