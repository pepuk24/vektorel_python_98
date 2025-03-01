def ekleme():
    with open("dosya.txt","a",encoding="utf8") as d:
        ad=input("adınızı girinız::\t\n"1)
        soyadı=input("soyadınınızı giriniz\n")
        nomara=(input("no giriniz....\n"))

        d.write(f"{ad},{soyadı},{nomara}\n")
   
def okuma():
    with open("dosya.txt","r",encoding="utf8") as d:
        okunacak=d.read()
    print(okunacak)


def listeleme():
    with open("dosya.txt","r") as m:
        
        k=m.readlines()
    print("dosya listesi")
    satir=1
    for satir in k:

        print(f"{satir} ",satir.strip())




def silme():
    with open("dosya.txt","r") as s:
        satirlar=s.readlines()
        print(satirlar)
    duzelt=input("lutfen silmek istediginiz alanı yazın").strip()
    yeni_satirlar=[]
    for satir in satirlar:
        if duzelt not in satirlar:
            yeni_satirlar.append(satir)
    with open("dosya.txt","w") as dosya:
        dosya.writelines(yeni_satirlar)




print(" 1 ekleme")
print(" 2 listeleme")
print(" 3 silme")
  
secim=input(r"Lutfen seçiminizi yapınız...")

if secim=="1":
    ekleme()
elif secim=="2":
    listeleme()
elif secim=="3":
    silme()

else:
    ("lUTFEN MENU ARALIGINDA SEÇİM YAPINIZ...")
   