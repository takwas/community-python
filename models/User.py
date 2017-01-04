from peewee import PrimaryKeyField, CharField, DateTimeField
import datetime
from models import BaseModel


class User(BaseModel):
    id = PrimaryKeyField()
    fname = CharField()
    sname = CharField()
    email = CharField(unique=True)
    profile_image_url = CharField(null=True)
    password = CharField()
    registered_on = DateTimeField(default=datetime.datetime.now)
