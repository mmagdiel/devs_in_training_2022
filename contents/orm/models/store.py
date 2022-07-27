import peewee
import datetime
from Connection import database

class Store(peewee.Model):
  admin = peewee.ForeignKeyField(User, related_name='store') #primary_key=True Relacion uno a uno
  name = peewee.CharField(max_length=50, unique=50, index=True)
  address = peewee.TextField()
  active = peewee.BooleanField(default=True)
  created_date = peewee.DateTimeField(default=datetime.datetime.now)
  
  class Meta:
    database = database
    db_table = 'stores'

  def __str__(self):
    return self.name