from models.main import create_tables
from controllers.products import insert_products
from controllers.categories import insert_categories
from controllers.stores import insert_stores
from controllers.users import insert_users


def create_schema():
  create_tables()
  insert_users()
  insert_stores()
  insert_products()
  insert_categories()
