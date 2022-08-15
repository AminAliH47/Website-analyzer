from peewee import Model, SqliteDatabase
from peewee import CharField

db = SqliteDatabase('database.db')


class BaseModel(Model):
    class Meta:
        database = db


class Token(BaseModel):
    code = CharField(max_length=6)


db.connect()
db.create_tables([Token])
