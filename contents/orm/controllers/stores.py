from models.store import Store

def insert_stores():
  Store.create(user_id=1, name='tienda uno', address='Oficina uno')
  Store.create(user_id=2, name='tienda dos', address='Oficinas dos')
