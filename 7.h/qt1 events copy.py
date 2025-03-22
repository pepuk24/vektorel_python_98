from PyQt6.QtWidgets import *

class ceviriPenceresi(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Çeviri")

        icerik = QVBoxLayout()
          #icerik = QHBoxLayout()
        icerik.addWidget(QLabel("Kullanıcı adı: "))
        self.kullanici_adi = QLineEdit() #
        icerik.addWidget(self.kullanici_adi) #
        self.buton = QPushButton("Çevir") #
        icerik.addWidget( QLabel("Şİfre: "))

        self.sifre = QLineEdit() #
        icerik.addWidget(self.sifre) #
        self.buton = QPushButton("Çevir") #
        icerik.addWidget(self.buton) #
        self.buton.clicked.connect(self.tiklama) #
        self.sonuc = QLabel("Sonuç: ")
        icerik.addWidget(self.sonuc)
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar) #

    def tiklama(self):
        # print("Tıklandı.")
        kullanicia = self.kullanici_adi.text()
        sifre = self.sifre.text()
        if kullanicia=="a" and sifre=="1":
            print("şifre doğru")
        else: print("Şifre yanlış, yetki yok.")

uygulama = QApplication([])

pencere = ceviriPenceresi()
pencere.show()

uygulama.exec() 
