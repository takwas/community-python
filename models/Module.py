from peewee import PrimaryKeyField, ForeignKeyField, DateField
from models import BaseModel, Module_Type
import datetime


class Module(BaseModel):
    id = PrimaryKeyField()
    type = ForeignKeyField(Module_Type, related_name='related_modules')
    build_on = DateField(default=datetime.datetime.now().date())