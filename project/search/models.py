from __future__ import unicode_literals
from django.db import models
import datetime
from infi.clickhouse_orm import Model
from django.db import models
from infi.clickhouse_orm import fields


class search_log(Model):
    timestamp = fields.DateTimeField()
    query = fields.StringField()
    print("type ", type(query))
    action = fields.StringField()
    tile_id = fields.Int32Field()
    user_agent = fields.StringField()


class Tile(models.Model):
 
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
 
    def __unicode__(self):
        return self.name
 
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
        }
