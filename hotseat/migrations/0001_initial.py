# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Terminal'
        db.create_table('hotseat_terminal', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
        ))
        db.send_create_signal('hotseat', ['Terminal'])

        # Adding model 'Assignment'
        db.create_table('hotseat_assignment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('terminal', self.gf('django.db.models.fields.related.ForeignKey')(related_name='assignments', to=orm['hotseat.Terminal'])),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('keepalive_token', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('keepalive_last', self.gf('django.db.models.fields.IntegerField')()),
            ('time_remaining', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('hotseat', ['Assignment'])


    def backwards(self, orm):
        # Deleting model 'Terminal'
        db.delete_table('hotseat_terminal')

        # Deleting model 'Assignment'
        db.delete_table('hotseat_assignment')


    models = {
        'hotseat.assignment': {
            'Meta': {'object_name': 'Assignment'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keepalive_last': ('django.db.models.fields.IntegerField', [], {}),
            'keepalive_token': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
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