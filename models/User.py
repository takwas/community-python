from peewee import CharField, DateTimeField, IntegerField, PrimaryKeyField
import datetime
from models import BaseModel
import random


class User(BaseModel):
    id = PrimaryKeyField()
    key = IntegerField(default=random.randint(999999, 2147483647), unique=True)
    fname = CharField()
    sname = CharField()
    email = CharField(unique=True)
    profile_image_url = CharField(null=True)
    password = CharField()
    registered_on = DateTimeField(default=datetime.datetime.now)
