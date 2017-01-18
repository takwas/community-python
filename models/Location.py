from peewee import PrimaryKeyField, CharField, DateField
from models import BaseModel
from datetime import datetime


class Location(BaseModel):
    id = PrimaryKeyField()
    city = CharField()
    address = CharField()
    available_from = DateField(default=datetime.now().strftime('%Y-%m-%d'))
    unavailable_from = DateField(null=True)