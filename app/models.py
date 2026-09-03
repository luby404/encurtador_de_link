from .core.database import orm, Model, db

class User(Model):
    ...

class Url(Model):
    url      = orm.CharField(max_length=1200)
    slug     = orm.CharField(max_length=256, unique=True)
    is_ative = orm.BooleanField(default=True)
    user     = orm.ForeignKeyField(User, backref="urls", null=True)

    clicks   = orm.IntegerField(default=-1)

class UrlAnalytic(Model):
    url  = orm.ForeignKeyField(Url, backref="url_analytics")
    user = orm.ForeignKeyField(User, backref="urls", null=True)


def init_models():
    db.connect()
    db.create_tables([User, Url, UrlAnalytic])

