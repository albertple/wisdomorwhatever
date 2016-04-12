# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FamousQuote'
        db.create_table(u'funnyquotes_famousquote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quote', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'funnyquotes', ['FamousQuote'])

        # Adding model 'InfamousQuote'
        db.create_table(u'funnyquotes_infamousquote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('add', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'funnyquotes', ['InfamousQuote'])


    def backwards(self, orm):
        # Deleting model 'FamousQuote'
        db.delete_table(u'funnyquotes_famousquote')

        # Deleting model 'InfamousQuote'
        db.delete_table(u'funnyquotes_infamousquote')


    models = {
        u'funnyquotes.famousquote': {
            'Meta': {'object_name': 'FamousQuote'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quote': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'funnyquotes.infamousquote': {
            'Meta': {'object_name': 'InfamousQuote'},
            'add': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['funnyquotes']