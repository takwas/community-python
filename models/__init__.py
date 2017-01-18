from peewee import MySQLDatabase, Model

db = MySQLDatabase('woodys_platform', user='root')


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


def initialize_db():
    db.create_tables([User, Group, Module_Type, Module, Role, User_Role], safe=True)


def close_db_connection():
    if not db.is_closed():
        db.close()
