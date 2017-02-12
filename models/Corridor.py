import uuid as uuid
from peewee import ForeignKeyField, PrimaryKeyField, CharField, UUIDField
from models import BaseModel


class Corridor(BaseModel):
    id = PrimaryKeyField()
    uuid = UUIDField(default=uuid.uuid4(), unique=True)
    # location = ForeignKeyField(Location, related_name='related_corridors')
    corridor = CharField()
