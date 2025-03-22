from PyQt6.QtWidgets import *

class anaPencere(QWidgets):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ana pencere")

        icerik = QVBoxLayout()
          #icerik = QHBoxLayout()
        icerik.addWidget(QLabel("Çevrilecek: "))
        icerik.addWidget(QLineEdit())
        icerik.addWidget(QPushButton("Çevir"))
        icerik.addWidget(QPushButton("Çevir"))
        icerik.addWidget(QPushButton("Çevir"))
        icerik.addWidget(QPushButton("Çevir"))
        icerik.addWidget(QLabel("Sonuç: "))
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

class ceviriPenceresi(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Çeviri")

        icerik = QVBoxLayout()
          #icerik = QHBoxLayout()
        icerik.addWidget(QLabel("Çevrilecek: "))
        icerik.addWidget(QLineEdit())
        icerik.addWidget(QPushButton("Çevir"))
        icerik.addWidget(QLabel("Sonuç: "))
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)
        pencere2 = anaPencere()
        pencere2.show()

uygulama = QApplication([])

pencere = ceviriPenceresi()
pencere.show()


uygulama.exec() 
