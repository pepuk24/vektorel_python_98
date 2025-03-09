def soyle(mesaj):
    print(mesaj)

# soyle("bugun hava çok guzel")


 
# def kisi_bilgisi(**bilgiler):
#     for anahtar, deger in bilgiler.items():
#         print(f"{anahtar}: {deger}")

# kisi_bilgisi(ad="Ali", yas=30, sehir="İstanbul")



# def kisi_bilgisi(**kwargs):
#     print(kwargs)  # kwargs'in içeriğini görelim

# kisi_bilgisi(ad="Ali", soyad="Kaya", yas=25, sehir="İstanbul", meslek="Mühendis")


# def kisi_bilgisi(**kwargs):
#     for heybe, katır in kwargs.items():  # kwargs sözlüğündeki her şeyi yazdır
#         print(f"{heybe}: {katır}")

# kisi_bilgisi(ad="Ali", soyad="Kaya", yas=25, sehir="İstanbul", meslek="Mühendis")


# def selam():
#     print ("merhaba ya muhammede")
#     def sabah():
#         print("günaydın")
#     sabah()

# selam()




saat =int(input("saat gir"))


def sabah():
       return "Günaydın"

def ogle():
    return "iyi günler"

def aksam():
    return "iyi aksamlar"

def gece():
    return "iyi uykular"

if saat<8:
    print("merhaba",sabah())
elif saat<18:
    print("iyi aksamlar", ogle())
elif saat < 18:
    print("iyi aksamlar")
else:
    print("merhaba",gece())    




