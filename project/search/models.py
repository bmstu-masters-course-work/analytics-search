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
