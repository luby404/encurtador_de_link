import peewee as orm


db = orm.SqliteDatabase("banco.db")

class Model(orm.Model):

    class Meta:
        database = db