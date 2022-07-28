import peewee
import datetime
from Connection import database

class Category(peewee.Model):
  name = peewee.CharField(max_length=100)
  description = peewee.TextField()
  created_date = peewee.DateTimeField(default=datetime.datetime.now)
  
  class Meta:
    database = database
    db_table = 'categories'

  def __str__(self):
    return '{name} - ${price}'.format(name=self.name, price=self.price)
