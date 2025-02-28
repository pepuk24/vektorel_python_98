#  Rehber Programi
import re,json,ast,io
dosya = open("RehberProgrami3.txt","a")
dosya.close()

def kayit_ekle():
    
    dosya = open("RehberProgrami3.txt","a")
    
    while True:
        isim = input("isim giriniz - Lütfen ç,ı,ş harflerini kullanmayin: ")
        soyad = input("soyad giriniz-Lütfen ç,ı,ş harflerini kullanmayin: ")
        numara = input("numara giriniz: ")
        
        
        dosya.write(str({"isim":isim,"soyad":soyad,"numara":numara})+",")
       # dosya.write(str({"isim":isim,"soyad":soyad,"numara":numara})+","+"\n") şeklinde 
       # yazarsak txt dosyasına alt alta yazıyor fakat listelemede sorun çıkarıyor.
       # Listelemede sorun olmaması için \n kullanmamak gerekiyor. 
         
        if devam_mi():
            continue
        else:
            break
        
dosya.close()

def emin_misin():
    a = input("emin misin (evet,hayir): ")
    if a.lower().startswith("e"):
        return True
    else:
        False


def devam_mi():
    a = input("devam etmek istiyor musun (evet,hayir): ")
    if a.lower().startswith("e"):
        return True
    else:
        False
        



def kayit_listele():
    dosya = open("RehberProgrami3.txt","r")
    okunan = dosya.read()
    cevirilen = ast.literal_eval(okunan)
    print(cevirilen)
    

def kayit_ara():
    dosya = open("RehberProgrami3.txt","r")
    okunan = dosya.read()
    cevirilen = ast.literal_eval(okunan)
    aranan = input("Aranan isim nedir?")
    for a in cevirilen:
        if a["isim"] == aranan : print(a) ; break
        
        # elif a["isim"]!= aranan : print("Bu isimde bir kayit yok.")
        # break
        # elif veya else eklediğimde aranan isim kısmını atlayıp bu isimde bir kayıt yok mesajı çıkıyor.
    
def duzeltme():
    dosya = open("RehberProgrami3.txt", "r")
    okunan = dosya.read()
    cevirilen = ast.literal_eval(okunan)
    aranan = input("Düzeltilecek isim nedir? ")
    dosya.close()
    with open("RehberProgrami3.txt","w") as dosya:
        for a in cevirilen:
            if a["isim"]==aranan:
                print(a)
                yeniAd = input("Yeni isim nedir? ")
                yeniSoyad = input("Yeni soyad nedir? ")
                yeniNo = input("Yeni numara nedir? ")
                a["isim"]=yeniAd
                a["soyad"]=yeniSoyad
                a["numara"]=yeniNo
            dosya.write(f"{str(a)},") 
      


def kayit_sil():
    dosya = open("RehberProgrami3.txt","r")
    okunan = dosya.read()
    cevirilen = ast.literal_eval(okunan)
    aranan = input("Silinecek isim nedir? ")
    dosya.close()
    with open("RehberProgrami3.txt","w") as silme:
        for a in cevirilen:
            if a["isim"]!=aranan:
                silme.write(f"{str(a)},")  
     

dosya.close()

while True:
    a = int(input("""
    1) kayit ekle
    2) kayitlari listele
    3) kayit ara
    4) kayit sil
    5) kayit düzeltme
    6) çikiş
    
    """))
    
    if a == 1:
        kayit_ekle()
    elif a == 2:
        kayit_listele()
    elif a == 3:
        kayit_ara()
    elif a == 4:
        kayit_sil()
    elif a == 5:
        duzeltme()
    elif a == 6:
        break