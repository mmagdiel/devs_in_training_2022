from models.user import User
from models.product import Product
from models.category import Category
from models.store import Store

def create_tables():
  if Category.table_exists():
    Category.drop_table()

  if Product.table_exists():
    Product.drop_table()

  if Store.table_exists():
    Store.drop_table()

  if User.table_exists():
    User.drop_table()

  User.create_table()
  Store.create_table()
  Product.create_table()
  Category.create_table()
