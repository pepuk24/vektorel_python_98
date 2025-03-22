# veritabanı sistemine bağlanmak için gerekli kodlar.
import mysql.connector

try:
  veri_tabanim = mysql.connector.connect(
    host="localhost", # Veritabanı sistemi adı (instance).
    # host="mysql.aktasweb.com", # Veritabanı sistemi adı (instance).
    user="root", # Veritabanı kullanıcı adı
    password="1234" # Veritabanı sistemi(instance) şifresi
  )
  print("Bağlantı tamam:")
  secilen = veri_tabanim.cursor()
#   secilen.execute("CREATE DATABASE pythondersleri") # SQL komutu
  secilen.execute("SHOW DATABASES")
  vt_listesi = secilen.fetchall()

  print(vt_listesi)



#   SHOW DATABASES
except:
  print("Veritabanına bağlanırken bir hata oluştu.")
# veritabanı sistemine bağlanma sistem kurulu değilse veya herhangi bir eksik varsa hata verecektir.
