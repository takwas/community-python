from peewee import CharField, DateTimeField, TextField, IntegerField, PrimaryKeyField
import datetime
from models import BaseModel
import random


class Group(BaseModel):
    id = PrimaryKeyField()
    key = IntegerField(default=random.randint(999999, 2147483647), unique=True)
    name = CharField()
    description = TextField()
    address = CharField(null=True)
    max_members = IntegerField(default=120)
    created_on = DateTimeField(default=datetime.datetime.now)
