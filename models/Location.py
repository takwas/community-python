from peewee import PrimaryKeyField, CharField, DateField, UUIDField, ForeignKeyField, SQL
from models import BaseModel, Location_Type
from datetime import datetime
import uuid


class Location(BaseModel):
    id = PrimaryKeyField()
    uuid = UUIDField(constraints=[SQL('DEFAULT uuid_generate_v4()')], unique=True)
    city = CharField()
    address = CharField()
    type = ForeignKeyField(Location_Type, related_name='related_locations')
    available_from = DateField(default=datetime.now().strftime('%Y-%m-%d'))
    unavailable_from = DateField(null=True)
