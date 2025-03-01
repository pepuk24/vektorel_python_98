# abc=open("dosyasistemi.txt","w",encoding="utf-8")
# abc.write("Dosyaya kaydedilen veri \n")
# abc.write("ucuncu satır")
# abc.write("w ile her çalıştıg")

# abc.close()

# f=open("demodosya.txt","a",encoding="utf-8")
# f.write("dosyaya ekleme yapma")
# f.write("her çalıştıgında içindekiler silinmez")
# f.close()

# f=open("demodosya.txt","r",encoding="utf=8")
# print(f.read())

# def anamenu():
#     print(okunan)
#     print(type(okunana))


def ekle():
    d=open("yenidosya.txt","a")

    print("ad giriniz",end="");ad=input()
    print("no giriniz",end="");no=input()

    d.write(f"{ad}{no}/n")
    d.close()

def oku():
    d=open("yenidosya.txt")
    okunan=d.read()