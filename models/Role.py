from peewee import PrimaryKeyField, CharField
from models import BaseModel

class Role(BaseModel):
    id = PrimaryKeyField()
    role = CharField()