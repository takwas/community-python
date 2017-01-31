from peewee import ForeignKeyField, DateField, CompositeKey
from models import BaseModel, Module, Location, db
import uuid


class Module_Location(BaseModel):
    module = ForeignKeyField(Module, related_name='locations')
    location = ForeignKeyField(Location, related_name='modules')
    start_date = DateField()
    end_date = DateField()


    class Meta:
        primary_key = CompositeKey('module', 'location', 'start_date')
