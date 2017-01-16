from peewee import PrimaryKeyField, ForeignKeyField, DateField
from models import BaseModel, Module_Type
import time


class Module(BaseModel):
    id = PrimaryKeyField()
    type = ForeignKeyField(Module_Type, related_name='module_type_id')
    build_on = DateField(default=time.strftime('%Y/%m/%d'))