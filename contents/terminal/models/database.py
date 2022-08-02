from sqlite3 import OperationalError, connect
from models.queries import build_table


class Database:
  def __init__(self, DATABASE):
    self.connection = connect(DATABASE)
  
  def create_table(self, model):
    try:
      self.connection.execute(build_table(model.name, model.create_schema()))
      print(f'se creo la tabla {model.name}')                        
    except OperationalError:
      print(f"La tabla {model.name} ya existe")  