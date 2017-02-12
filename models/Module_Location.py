from peewee import ForeignKeyField, DateField, CompositeKey, FloatField, UUIDField, SQL
from models import BaseModel, Module, Location, Corridor
import uuid


class Module_Location(BaseModel):
    uuid = UUIDField(constraints=[SQL('DEFAULT uuid_generate_v4()')], unique=True)
    module = ForeignKeyField(Module, related_name='locations')
    location = ForeignKeyField(Location, related_name='modules')
    corridor = ForeignKeyField(Corridor, related_name='modules')
    price_per_month = FloatField()
    start_date = DateField()
    end_date = DateField()

    class Meta:
        primary_key = CompositeKey('module', 'start_date')
