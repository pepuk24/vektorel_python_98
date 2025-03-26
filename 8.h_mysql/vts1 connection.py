# mysql-connector-python
import mysql.connector as vtys

try:
    vts = vtys.connect(
        host="localhost", # Server.
        user="root", # Kullanıcı adı.
        password="1234" # Şifre 
    )
    print("Bağlantı tamam.")

except:
    print("Bağlantı yapılamadı.")



