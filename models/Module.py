from peewee import PrimaryKeyField, ForeignKeyField, DateField, UUIDField, SQL
from models import BaseModel, Module_Type
import datetime


class Module(BaseModel):
    id = PrimaryKeyField()
    uuid = UUIDField(constraints=[SQL('DEFAULT uuid_generate_v4()')], unique=True)
    type = ForeignKeyField(Module_Type, related_name='related_modules')
    build_on = DateField(default=datetime.datetime.now().date())