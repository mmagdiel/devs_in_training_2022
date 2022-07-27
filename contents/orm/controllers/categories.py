from models.category import Category

def insert_categories():
  Category.create(name='Liquidos', description='liquidos')
  Category.create(name='Embutidos', description='embutidos')
  Category.create(name='Snacks', description='snacks')
  Category.create(name='Aderezos', description='aderezos')
  Category.create(name='Carnes', description='carnes')
