# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Assignment.created'
        db.add_column('hotseat_assignment', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'Assignment.last_updated'
        db.add_column('hotseat_assignment', 'last_updated',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Assignment.created'
        db.delete_column('hotseat_assignment', 'created')

        # Deleting field 'Assignment.last_updated'
        db.delete_column('hotseat_assignment', 'last_updated')


    models = {
        'hotseat.assignment': {
            'Meta': {'object_name': 'Assignment'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keepalive_last': ('django.db.models.fields.IntegerField', [], {}),
            'keepalive_token': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'terminal': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'assignments'", 'to': "orm['hotseat.Terminal']"}),
            'time_remaining': ('django.db.models.fields.IntegerField', [], {})
        },
        'hotseat.terminal': {
            'Meta': {'object_name': 'Terminal'},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'})
        }
    }

    complete_apps = ['hotseat']