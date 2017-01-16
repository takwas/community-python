from peewee import PrimaryKeyField, CharField
from models import BaseModel


class Module_Type(BaseModel):
    id = PrimaryKeyField()
    type = CharField()
