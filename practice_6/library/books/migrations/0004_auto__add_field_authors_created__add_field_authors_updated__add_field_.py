# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Authors.created'
        db.add_column('books_authors', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(blank=True, default=datetime.datetime.now, auto_now_add=True),
                      keep_default=False)

        # Adding field 'Authors.updated'
        db.add_column('books_authors', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(blank=True, default=datetime.datetime.now, auto_now=True),
                      keep_default=False)

        # Adding field 'Book.created'
        db.add_column('books_book', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(blank=True, default=datetime.datetime.now, auto_now_add=True),
                      keep_default=False)

        # Adding field 'Book.updated'
        db.add_column('books_book', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(blank=True, default=datetime.datetime.now, auto_now=True),
                      keep_default=False)

        # Adding field 'Publisher.created'
        db.add_column('books_publisher', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(blank=True, default=datetime.datetime.now, auto_now_add=True),
                      keep_default=False)

        # Adding field 'Publisher.updated'
        db.add_column('books_publisher', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(blank=True, default=datetime.datetime.now, auto_now=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Authors.created'
        db.delete_column('books_authors', 'created')

        # Deleting field 'Authors.updated'
        db.delete_column('books_authors', 'updated')

        # Deleting field 'Book.created'
        db.delete_column('books_book', 'created')

        # Deleting field 'Book.updated'
        db.delete_column('books_book', 'updated')

        # Deleting field 'Publisher.created'
        db.delete_column('books_publisher', 'created')

        # Deleting field 'Publisher.updated'
        db.delete_column('books_publisher', 'updated')


    models = {
        'books.authors': {
            'Meta': {'object_name': 'Authors'},
            'birthyear': ('django.db.models.fields.SmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now', 'auto_now_add': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now', 'auto_now': 'True'})
        },
        'books.book': {
            'Meta': {'object_name': 'Book'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['books.Authors']", 'symmetrical': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {}),
            'publishers': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['books.Publisher']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now', 'auto_now': 'True'})
        },
        'books.publisher': {
            'Meta': {'object_name': 'Publisher'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now', 'auto_now': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['books']