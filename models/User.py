from peewee import PrimaryKeyField, CharField
from models import BaseModel


class User(BaseModel):
    id = PrimaryKeyField()
    fname = CharField()
    sname = CharField()
    email = CharField(unique=True)
    profile_image_url = CharField(null=True)
    password = CharField()
