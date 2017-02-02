from peewee import Model, PostgresqlDatabase
import sys

db = PostgresqlDatabase('woodys_platform', user='postgres')


class BaseModel(Model):
    class Meta:
        database = db


# TODO: BaseModel Import fix
# Import models here
from .User import User
from .Group import Group
from .Module_Type import Module_Type
from .Module import Module
from .Role import Role
from .User_Role import User_Role
from .Location import Location
from .Module_Location import Module_Location
from .Contract import Contract


def initialize_db():
    db.connect()
    db.create_tables([User, Group, Module_Type, Module, Role, User_Role, Location, Module_Location, Contract], safe=True)


def close_db_connection():
    if not db.is_closed():
        db.close()
