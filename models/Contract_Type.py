from peewee import PrimaryKeyField, CharField, UUIDField
from models import BaseModel
import uuid


class Contract_Type(BaseModel):
    id = PrimaryKeyField()
    uuid = UUIDField(default=uuid.uuid4(), unique=True)
    type = CharField()
