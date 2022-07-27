from models.user import User

def insert_users():
  User.create(username='mmagdiel', password='1234567', email='mmagdiel@gmail.com')
  User.create(username='ccamilo', password='7891234', email='ccamilo@gmail.com')
