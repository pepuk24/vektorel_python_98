# mysql-connector-python
import mysql.connector as vtys

try:
    vts = vtys.connect(
        host="localhost", # Server.
        user="root", # Kullanıcı adı.
        password="1234" # Şifre 
    )
    print("Bağlantı tamam.")
    secilen = vts.cursor()
    secilen.execute('SHOW DATABASES')
    vt_listesi = secilen.fetchall()
    print(*vt_listesi,sep="\n")

except:
    print("Bağlantı yapılamadı.")



