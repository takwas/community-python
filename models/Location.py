from peewee import PrimaryKeyField, CharField, DateField, UUIDField, SQL
from models import BaseModel
from datetime import datetime
import uuid


class Location(BaseModel):
    id = PrimaryKeyField()
    uuid = UUIDField(default=uuid.uuid4(), unique=True)
    city = CharField()
    address = CharField()
    available_from = DateField(default=datetime.now().strftime('%Y-%m-%d'))
    unavailable_from = DateField(null=True)