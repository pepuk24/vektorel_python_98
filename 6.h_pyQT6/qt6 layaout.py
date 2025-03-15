from PyQt6.QtWidgets import *

uygulama = QApplication([])
pencere = QMainWindow()


icerik = QVBoxLayout()
icerik.addWidget(QLineEdit())
icerik.addWidget(QLineEdit())
icerik.addWidget(QLineEdit())

nesne = QHBoxLayout()
nesne.addWidget(QPushButton("buton"))
nesne.addWidget(QPushButton("buton"))
nesne.addWidget(QPushButton("buton"))
nesne.addWidget(QPushButton("buton"))
nesne.addWidget(QPushButton("buton"))
icerik.addLayout(nesne)

icerik.addWidget(QLabel("label"))
icerik.addWidget(QLabel("label"))

# icerik.addLayout(dugmeler)
araclar = QWidget()
araclar.setLayout(icerik)
pencere.setCentralWidget(araclar)
pencere.show()

uygulama.exec()