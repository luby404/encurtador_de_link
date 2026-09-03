import peewee as orm
from datetime import datetime

db = orm.SqliteDatabase("banco.db")

class Model(orm.Model):

    criado_em = orm.DateTimeField(default=datetime.now)

    class Meta:
        database = db