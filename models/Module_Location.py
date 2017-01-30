from peewee import ForeignKeyField, DateField, PrimaryKeyField, CompositeKey
from models import BaseModel, Module, Location
from datetime import datetime


class Module_Location(BaseModel):
    module = ForeignKeyField(Module, related_name='locations')
    location = ForeignKeyField(Location, related_name='modules')
    start_date = DateField()
    end_date = DateField()


    class Meta:
        primary_key = CompositeKey('module', 'location', 'start_date')