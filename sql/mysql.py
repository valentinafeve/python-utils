import mysql.connector

mydb = mysql.connector.connect(
	host="200.3.149.139",
	user="yatek",
	password="bunterWind45"
)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
