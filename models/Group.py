from peewee import PrimaryKeyField, CharField, DateTimeField, TextField, IntegerField
import datetime
from models import BaseModel


class Group(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    description = TextField()
    address = CharField()
    max_members = IntegerField(default=120)
    created_on = DateTimeField(default=datetime.datetime.now)
