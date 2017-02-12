from peewee import ForeignKeyField, UUIDField, SQL
from models import BaseModel, User, Role


class User_Role(BaseModel):
    uuid = UUIDField(constraints=[SQL('DEFAULT uuid_generate_v4()')], unique=True)
    user = ForeignKeyField(User, related_name='assigned_roles')
    role = ForeignKeyField(Role, related_name='assigned_roles')