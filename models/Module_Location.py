from peewee import ForeignKeyField, DateField, PrimaryKeyField, CompositeKey
from models import BaseModel, Module, Location
from datetime import datetime


class Module_Location(BaseModel):
    module = ForeignKeyField(Module, related_name='locations')
    location = ForeignKeyField(Location, related_name='modules')
    start_date = DateField(default=datetime.now())
    end_date = DateField(null=True)


    class Meta:
        primary_key = CompositeKey('module', 'location', 'start_date')