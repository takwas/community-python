from peewee import PrimaryKeyField, ForeignKeyField, DateField, UUIDField, SQL
from models import BaseModel, Module_Type
import datetime
import uuid


class Module(BaseModel):
    id = PrimaryKeyField()
    uuid = UUIDField(constraints=[SQL('DEFAULT uuid_generate_v1()')], unique=True)
    type = ForeignKeyField(Module_Type, related_name='related_modules')
    build_on = DateField(default=datetime.datetime.now().date())