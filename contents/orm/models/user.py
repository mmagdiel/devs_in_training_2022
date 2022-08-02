import peewee
import datetime
from Connection import database

class User(peewee.Model):
  username = peewee.CharField(unique=True, max_length=50, index=True)
  password = peewee.CharField(max_length=50, null=True)
  email = peewee.CharField(max_length=50)
  active = peewee.BooleanField(default=True)
  created_date = peewee.DateTimeField(default=datetime.datetime.now)

  class Meta:
    database = database
    db_table = 'users'

  def __str__(self):
    return self.username