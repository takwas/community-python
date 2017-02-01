from peewee import DateField, ForeignKeyField, CompositeKey
from models import BaseModel, User, Module
from datetime import datetime


class Contract(BaseModel):
    user = ForeignKeyField(User, related_name='contracts')
    module = ForeignKeyField(Module, related_name='contracts')
    signed_on = DateField(default=datetime.now().date())
    valid_til = DateField()

    class Meta:
        primary_key = CompositeKey('user', 'module', 'signed_on')
