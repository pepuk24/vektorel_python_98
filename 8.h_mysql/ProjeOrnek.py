import mysql.connector
from PyQt6.QtWidgets import *

kullanicilar =[]

try:
    vts = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1234",
        database = "okultakipsistemi"
    )
    print("Bağlantı tamam.")
    secilenVT = vts.cursor()
    # secilenVT.execute("SELECT * FROM kullanicilar")
    # kullanicilar = secilenVT.fetchall()
    print(kullanicilar)

except Exception as hata:
    print("Sorun oluştu: ", hata)

class AnaEkran(QMainWindow):
    def __init__(self):
        super().__init__()       

        self.setWindowTitle("Giriş ekranı")
       
        icerik = QVBoxLayout()
        icerik.addWidget(QLabel("Kullanıcı adı: "))

        self.buton1 = QPushButton("Modul-xx")
        icerik.addWidget(self.buton1)
        self.buton2 = QPushButton("Modul-xx")
        icerik.addWidget(self.buton2)
        self.buton3 = QPushButton("Modul-xx")
        icerik.addWidget(self.buton3)
       
       
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)


class LoginEkrani(QMainWindow):
    def __init__(self):
        super().__init__()       

        self.setWindowTitle("Giriş ekranı")
       
        icerik = QVBoxLayout()
        icerik.addWidget(QLabel("Kullanıcı adı: "))

        self.kullanici_adi = QLineEdit()
        icerik.addWidget(self.kullanici_adi)
       
        icerik.addWidget(QLabel("Şifre: "))
        self.sifre = QLineEdit()
        icerik.addWidget(self.sifre)
       
        self.buton = QPushButton("Giriş yap")
        icerik.addWidget(self.buton)
       
        self.buton.clicked.connect(self.kontrolEt)
       
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

    def kontrolEt(self):
        secilenVT.execute("SELECT * FROM kullanicilar")
        kullanicilar = secilenVT.fetchall()
        # print("Kontrol kullanıclar:", kullanicilar)
        ka = self.kullanici_adi.text()
        sf = self.sifre.text()
        for aa in kullanicilar:
            # print(f"KA:{aa[0]}, ŞF:{aa[1]}")
            if ka==aa[0] and sf==aa[1]:
                self.anaEkran = AnaEkran()
                self.anaEkran.show()
                self.close()
                print("PROGRAMA GİRİLDİ")
            else:
                print("Kullanım yetkiniz yok")
                self.close()


app = QApplication([])
girisEkrani = LoginEkrani()
girisEkrani.show()
app.exec()