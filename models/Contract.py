from peewee import DateField, ForeignKeyField, CompositeKey, UUIDField, SQL
from models import BaseModel, User, Module, Contract_Type
from datetime import datetime
import uuid


class Contract(BaseModel):
    uuid = UUIDField(default=uuid.uuid4(), constraints=[SQL('DEFAULT uuid_generate_v4()')], unique=True)
    user = ForeignKeyField(User, related_name='contracts')
    module = ForeignKeyField(Module, related_name='contracts')
    type = ForeignKeyField(Contract_Type, related_name='contracts')
    signed_on = DateField(default=datetime.now().date())
    valid_till = DateField()

    class Meta:
        primary_key = CompositeKey('user', 'module', 'signed_on')
