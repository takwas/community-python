from peewee import CharField, UUIDField, PrimaryKeyField, SQL
from models import BaseModel


class Module_Type(BaseModel):
    id = PrimaryKeyField()
    uuid = UUIDField(constraints=[SQL('DEFAULT uuid_generate_v4()')], unique=True)
    type = CharField()
