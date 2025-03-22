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
  print(veri_tabanim) 
  print(veri_tabanim.user) 
  print(veri_tabanim.database) 
  print(veri_tabanim.connection_id) 
except:
  print("Veritabanına bağlanırken bir hata oluştu.")
# veritabanı sistemine bağlanma sistem kurulu değilse veya herhangi bir eksik varsa hata verecektir.
