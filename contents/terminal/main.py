import sqlite3
from env import DATABASE
import typer

def main(name: str):
    print(f"Hello {name}")

if __name__ == '__main__':
  connection = sqlite3.connect(DATABASE)
  cursor = connection.cursor()
  try:
    connection.execute("""create table articulos (
                              codigo integer primary key autoincrement,
                              descripcion text,
                              precio real
                        )""")
    print("se creo la tabla articulos")                        
  except sqlite3.OperationalError:
    print("La tabla articulos ya existe")  
  typer.run(main)
  connection.close()
  