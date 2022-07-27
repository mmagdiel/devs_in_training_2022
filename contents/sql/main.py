import MySQLdb
from env import HOST, USER, PASSWORD, DATABASE
from queries import USERSTABLE, DROPUSERTABLE, SHOWTABLES, INSERTUSER, SELECTUSER

if __name__ == '__main__':
  connection = MySQLdb.connect(HOST, USER, PASSWORD, DATABASE)
  cursor = connection.cursor()
  
  cursor.execute(DROPUSERTABLE)
  cursor.execute(USERSTABLE)
  cursor.execute(SHOWTABLES)
  tables = cursor.fetchall()
  
  for table in tables:
    print(table[0])
  
  query = INSERTUSER.format(username='mmagdiel', password='1234567')
  print(query)
  
  try:
    cursor.execute(query)
    connection.commit()
  except:
    db.rollback()

  query = SELECTUSER.format(id=1)
  cursor.execute(query)
  
  results = cursor.fetchall()
  user = results[0]
    
  print("username : " + user[1])
  print("password : " + user[2])

  connection.close()
  



