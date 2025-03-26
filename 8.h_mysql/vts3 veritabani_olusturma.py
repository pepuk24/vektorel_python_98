# mysql-connector-python
# Bağlan
# cursor ile seç
# sql çalıştır.
# eğer veri çekeceksek fetch
# eğer bilgi kayıt/değiştirme yapılacaksa commit

import mysql.connector as vtys

try:
    vts = vtys.connect(
        host="localhost", # Server.
        user="root", # Kullanıcı adı.
        password="1234" # Şifre 
    )
    print("Bağlantı tamam.")
    secilen = vts.cursor() # IF NOT EXISTS
    secilen.execute('create database deneme') # yoksa oluturur, varsa hata verir
    # secilen.execute('create database if not exists deneme') # varsa çalışmaz
    vt_listesi = secilen.fetchall()
    # print(*vt_listesi,sep="\n")
    # print(vt_listesi)

except Exception as e:
    print("Bağlantı yapılamadı.",e)



