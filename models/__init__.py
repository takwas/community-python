from peewee import PostgresqlDatabase, SqliteDatabase, MySQLDatabase, Model

# db = PostgresqlDatabase('woodys_platform', user='theobouwman')
# db = SqliteDatabase(os.getcwd() + '/community.db')
db = MySQLDatabase('woodys_platform', user='root', password='rootroot')


class BaseModel(Model):
    class Meta:
        database = db


# TODO: BaseModel Import fix
# Import models here
from User import User
from Group import Group
from Module_Type import Module_Type
from Module import Module


def initialize_db():
    db.create_tables([User, Group, Module_Type, Module], safe=True)


def close_db_connection():
    if not db.is_closed():
        db.close()
