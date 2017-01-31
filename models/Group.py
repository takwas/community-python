from peewee import CharField, DateTimeField, TextField, IntegerField, PrimaryKeyField, UUIDField, SQL
import datetime
from models import BaseModel
import random
import uuid


class Group(BaseModel):
    id = PrimaryKeyField()
    uuid = UUIDField(constraints=[SQL('DEFAULT uuid_generate_v1()')], unique=True)
    name = CharField()
    description = TextField()
    address = CharField(null=True)
    max_members = IntegerField(default=120)
    created_on = DateTimeField(default=datetime.datetime.now)
