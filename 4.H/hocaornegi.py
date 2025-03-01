import hocaornegi_oku1

def wexina():
    d=open("hocadosya.txt","a")
    
    nav=print("adınızı gir",end="");nav=input()
    soy=print("soyad",end="");soy=input()
    nomara=print("numara",end="");nomara=input()
    d.write(f"{nav}|{soy}|{nomara}\n")
    d.close()
def oku():
    with open("hocadosya.txt","r") as filla:
      okunan=filla.read()
      print(okunan)


def anamenu():
   print("REHBER LİSTESİ")
   print("1 ekle")
   print("2 listele")
   print("3 listele1")
   print("4 sil")
   menuler= input()
   if menuler=="1":
        wexina()
   elif  menuler=="2":
        oku()
   elif menuler=="3":
         hocaornegi_oku1.oku1()

anamenu()