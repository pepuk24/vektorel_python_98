import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="okultakipsistemi"
)

mycursor = mydb.cursor()
sql = "select * from ogrenciler"

mycursor.execute(sql)
okunanlar = mycursor.fetchall()
print(*okunanlar, sep="\n")

