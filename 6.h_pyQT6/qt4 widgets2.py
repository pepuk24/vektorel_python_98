from PyQt6.QtWidgets import *

uygulama = QApplication([])

pencere = QMainWindow()
pencere.setWindowTitle("Çeviri")

icerik = QVBoxLayout()
# icerik = QHBoxLayout()
icerik.addWidget(QLabel("Kullanıcı adı: "))
icerik.addWidget(QLineEdit("Ka yaz"))
icerik.addWidget(QLabel("Şİfre: "))
icerik.addWidget(QLineEdit("Şifre yaz"))

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