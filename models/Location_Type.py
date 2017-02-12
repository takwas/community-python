from peewee import PrimaryKeyField, CharField, UUIDField, SQL
from models import BaseModel


class Location_Type(BaseModel):
    id = PrimaryKeyField()
    uuid = UUIDField(constraints=[SQL('DEFAULT uuid_generate_v4()')], unique=True)
    type = CharField()
