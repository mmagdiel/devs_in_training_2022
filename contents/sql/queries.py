USERSTABLE = """CREATE TABLE users ( 
         id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
         username VARCHAR(50) NOT NULL,
         password VARCHAR(50) NOT NULL
         )"""

DROPUSERTABLE = "DROP TABLE IF EXISTS `users`"
SHOWTABLES = "SHOW TABLES"

INSERTUSER = "INSERT INTO users (username, password) VALUES( '{username}', '{password}' );"
SELECTUSER = "SELECT * FROM users WHERE Id = {id}"