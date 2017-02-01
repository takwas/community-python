from typing import Dict
from peewee import CharField, DateTimeField, UUIDField, PrimaryKeyField, SQL, BooleanField
import datetime
from playhouse.shortcuts import dict_to_model
from models import BaseModel
import secrets


class User(BaseModel):
    id = PrimaryKeyField()
    uuid = UUIDField(constraints=[SQL('DEFAULT uuid_generate_v1()')], unique=True)
    fname = CharField()
    sname = CharField()
    email = CharField(unique=True)
    profile_image_url = CharField(null=True)
    password = CharField()
    activated = BooleanField(default=False)
    activation_key = CharField(default=secrets.token_urlsafe())
    registered_on = DateTimeField(default=datetime.datetime.now)

    @staticmethod
    def from_oject(user: Dict):
        """
        returns a User object from a dictionary (used for session user)
        """
        return dict_to_model(data=user, model_class=User)
