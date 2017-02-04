from peewee import PrimaryKeyField, ForeignKeyField
from models import BaseModel, User, Role


class User_Role(BaseModel):
    id = PrimaryKeyField()
    user = ForeignKeyField(User, related_name='assigned_roles')
    role = ForeignKeyField(Role, related_name='assigned_roles')