from peewee import CharField, DateTimeField, TextField, IntegerField, PrimaryKeyField, UUIDField
import datetime
from models import BaseModel
import random
import uuid


class Group(BaseModel):
    id = PrimaryKeyField()
    uuid = UUIDField(default=uuid.uuid1())
    name = CharField()
    description = TextField()
    address = CharField(null=True)
    max_members = IntegerField(default=120)
    created_on = DateTimeField(default=datetime.datetime.now)
