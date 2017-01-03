from peewee import PostgresqlDatabase, SqliteDatabase, Model
import os

# db = PostgresqlDatabase('community', user='theobouwman')
db = SqliteDatabase(os.getcwd() + '/community.db')


class BaseModel(Model):
    class Meta:
        database = db


# TODO: BaseModel Import fix
# Import models here
from User import User


def initialize_db():
    db.create_tables([User], safe=True)


def close_db_connection():
    if not db.is_closed():
        db.close()
