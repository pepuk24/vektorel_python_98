# mysql-connector-python
# Bağlan
# cursor ile seç
# sql çalıştır.
# eğer veri çekeceksek fetch
# eğer bilgi kayıt/değiştirme yapılacaksa commit

import mysql.connector as vtys

try:
    vts1 = vtys.connect(
        host="localhost", # Server.
        user="root", # Kullanıcı adı.
        password="1234", # Şifre 
        database="pythondersleri"
    )
    
    print("Bağlantı tamam.")
    secilen = vts1.cursor() # sql komutlarında use yerine geçer
    # vts1.database = ""
    # secilen.execute("use databaseadi")
    
    secilen.execute("CREATE TABLE ogrenciler1 (ad VARCHAR(255), telefon VARCHAR(255))")

except Exception as e:
    print("Bağlantı yapılamadı.",e)