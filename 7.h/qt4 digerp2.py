from PyQt6.QtWidgets import * 
from random import randint

class AnaPencere(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ana Ekran")
        
        icerik = QVBoxLayout()
        baslik = QLabel("PROGRAM ANA EKRANI")
        baslik.setStyleSheet("border: 1px solid blue; color: red; font-size:20px")
        icerik.addWidget(baslik)

        self.buton1 = QPushButton("Uygulama -1")
        self.buton2 = QPushButton("Uygulama -2")
        self.buton3 = QPushButton("Uygulama -3")
        self.buton4 = QPushButton("Uygulama -4")
        
        icerik.addWidget(self.buton1)
        icerik.addWidget(self.buton2)
        icerik.addWidget(self.buton3)
        icerik.addWidget(self.buton4)
        
        araclar = QWidget() # QWidget aracılığıyla layout'u yerleştir
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)  # Ana pencereye yerleştir

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
        ka = self.kullanici_adi.text()
        sf = self.sifre.text()
        if ka=="1" and sf=="1":
            self.anaEkran = AnaPencere()
            self.anaEkran.show()
            self.close()
        else:
            print("kullanım yetkiniz yok")
            self.close()

app = QApplication([])
girisEkrani = LoginEkrani()
girisEkrani.show()



app.exec()
