import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="secret-pw",
    database= "todolist"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE todo (id INT AUTO_INCREMENT PRIMARY KEY, task VARCHAR(255), progress (VARCHAR)) DEFAULT 'not started', ")
