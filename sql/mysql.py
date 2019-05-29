import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="albino bear"
)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
mycursor.execute("SELECT * FROM PEOPLE")
