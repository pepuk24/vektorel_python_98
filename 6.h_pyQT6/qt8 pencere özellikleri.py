from PyQt6.QtWidgets import *
from PyQt6.QtCore import QSize, Qt
from PyQt6 import QtGui

class ceviriPenceresi(QMainWindow):
    def __init__(self,pb="Çeviri",bs=1):
        super().__init__()
        self.setWindowTitle(pb)
        # self.setFixedSize(QSize(400, 300))
        self.setWindowIcon(QtGui.QIcon('vue.png'))

        icerik = QVBoxLayout()
        icerik.addWidget(QLabel("Çevrilecek: "))
        icerik.addWidget(QLineEdit())
        icerik.addWidget(QPushButton("Çevir"))
        icerik.addWidget(QLabel("Sonuç: "))
        for a in range(bs):
            icerik.addWidget(QPushButton(f"{a+1}.buton"))
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

uygulama = QApplication([])

pencere = ceviriPenceresi()
pencere.show()
pencere1 = ceviriPenceresi("Deneme",50)
pencere1.show()

uygulama.exec() 
