import peewee
from env import DATABASE, HOST, PORT, USER, PASSWD

database = peewee.MySQLDatabase(DATABASE, host=HOST, port=PORT, user=USER, passwd=PASSWD)
