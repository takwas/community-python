from peewee import CharField, DateTimeField, TextField, IntegerField, PrimaryKeyField, UUIDField, SQL
import datetime
from models import BaseModel


class Group(BaseModel):
    id = PrimaryKeyField()
    uuid = UUIDField(constraints=[SQL('DEFAULT uuid_generate_v4()')], unique=True)
    name = CharField()
    description = TextField()
    address = CharField(null=True)
    max_members = IntegerField(default=120)
    created_on = DateTimeField(default=datetime.datetime.now)
