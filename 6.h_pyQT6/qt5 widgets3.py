from PyQt6.QtWidgets import *

uygulama = QApplication([])

pencere = QMainWindow()
pencere.setWindowTitle("Çeviri")

icerik = QVBoxLayout()
# icerik = QHBoxLayout()

ka = QHBoxLayout()
ka.addWidget(QLabel("Kullanıcı adı: "))
ka.addWidget(QLineEdit())
icerik.addLayout(ka)

sf = QHBoxLayout()
sf.addWidget(QLabel("Şifre: "))
sf.addWidget(QLineEdit("Şifre yaz"))
icerik.addLayout(sf)

dugmeler = QHBoxLayout()
dugmeler.addWidget(QPushButton("Giriş yap"))
dugmeler.addWidget(QPushButton("Vazgeç"))
dugmeler.addWidget(QPushButton("Çıkış"))

icerik.addLayout(dugmeler)
araclar = QWidget()
araclar.setLayout(icerik)
pencere.setCentralWidget(araclar)
pencere.show()

uygulama.exec()