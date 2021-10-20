from __future__ import unicode_literals
from django.db import models
import datetime
 
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
