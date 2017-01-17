from peewee import PrimaryKeyField, ForeignKeyField
from models import BaseModel, User, Role

class User_Role(BaseModel):
    id = PrimaryKeyField()
    user = ForeignKeyField(User, related_name='user_role_user_id')
    role = ForeignKeyField(Role, related_name='user_role_role_id')