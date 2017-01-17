from peewee import PrimaryKeyField, ForeignKeyField, DateTimeField
from models import BaseModel, Module_Type
import datetime


class Module(BaseModel):
    id = PrimaryKeyField()
    type = ForeignKeyField(Module_Type, related_name='module_type_id')
    build_on = DateTimeField(default=datetime.datetime.now())