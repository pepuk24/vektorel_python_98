from PyQt6.QtWidgets import *

class ceviriPenceresi(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Çeviri")

        icerik = QVBoxLayout()
          #icerik = QHBoxLayout()
        icerik.addWidget(QLabel("Çevrilecek: "))
        self.cevirilecek = QLineEdit() #
        icerik.addWidget(self.cevirilecek) #
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
        yazilacak = self.cevirilecek.text()
        print(int(yazilacak)*2)
        mevcut = self.sonuc.text()
        self.sonuc.setText(mevcut + str(int(yazilacak)*2))

uygulama = QApplication([])

pencere = ceviriPenceresi()
pencere.show()

uygulama.exec() 
