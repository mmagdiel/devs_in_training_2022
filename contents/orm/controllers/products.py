from models.product import Product

def insert_products():
  Product.create(store_id=1, name='Pan', description='Pan integral', price=5.5, stock=50)
  Product.create(store_id=1, name='Leche', description='Baja en gradas', price=15.5, stock=100)
  Product.create(store_id=1, name='Jamon', description='de pavo', price=30.9, stock=80)
  Product.create(store_id=1, name='mayonesa', description='mayonesa', price=30.9, stock=80)

  Product.create(store_id=2, name='Soda', description='Dieta', price=10.0, stock=50)
  Product.create(store_id=2, name='Fritura', description='Frituras de papa', price=20.5, stock=100)
  Product.create(store_id=2, name='Salsa', description='chile habanero', price=29, stock=80)
  Product.create(store_id=2, name='Mostaza', description='Mostaza', price=30.9, stock=80)
