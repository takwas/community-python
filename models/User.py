from peewee import CharField, DateTimeField, UUIDField, PrimaryKeyField
import datetime
from models import BaseModel
import uuid


class User(BaseModel):
    id = PrimaryKeyField()
    uuid = UUIDField(default=uuid.uuid1())
    fname = CharField()
    sname = CharField()
    email = CharField(unique=True)
    profile_image_url = CharField(null=True)
    password = CharField()
    registered_on = DateTimeField(default=datetime.datetime.now)
