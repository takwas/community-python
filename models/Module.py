from peewee import PrimaryKeyField, ForeignKeyField, DateField, UUIDField, SQL
from models import BaseModel, Module_Type
import datetime
import uuid


class Module(BaseModel):
    id = PrimaryKeyField()
    uuid = UUIDField(default=uuid.uuid4(), unique=True)
    type = ForeignKeyField(Module_Type, related_name='related_modules')
    build_on = DateField(default=datetime.datetime.now().date())