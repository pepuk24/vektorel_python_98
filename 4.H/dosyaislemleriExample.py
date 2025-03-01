# abc=open("rehberr.txt","w",encoding="utf8")

# abc.write("Dosyaya kaydedilen veri")

# abc.write("buda 3.satir,ama ilk ve ikinci satir yok dikkat et silinmiş")
# abc.close()



# #Dosyaya ekleme yapma


# f=open("demofile","a",encoding="utf8")
# f.write("bu 1.satir\n")
# f.write("Bu ikinci satir,bu arada dikkat et veriler silinmiyor\n")
# f.write("bu son 3. satir bundan sonra yeni dosyaya ekleme yapılacak...")
# f.close()


#EKLEME SONRASI DOSYA İÇERİGİNE BAKMA

k=open("demofile","r",encoding="utf8")

# içerik=k.read()
# print(içerik)
# k.close()   #Dosyayı kapatmayı unutma....   #Bu yontem dosyanın tamamını bir "string" olarak ele alır.......



# k=open("demofile","r",encoding="utf8")  #satır satır okuma....
# for satir in k:
#     print(satir.strip())  #satir sonundaki bosluklar kaldirilir....
# k.clos() #Burda dikkkat etmen gereken nokte k.close yazdıktan sonra artik bir işlem yapamazsın oyle bir durumda k.close kaldırp işlemi yaptiktan sonra dekrardan koymandır...



# l=open("demofile","r",encoding="utf-8")   #Satırları liste olarak okumma
# satirlar=k.readlines()    #Her satiri bir liste öğesi olarak ele alır
# print(satirlar)          
# k.close

# with open("demofile","r",encoding="utf8") as t:
#     içerik=k.read()
#     print(içerik)



# with open("ext.txt","w",encoding="utf8") as xxx:
#     xxx.write("ext.txt")


# f=open("ext.txt","r")
# print(f.read()) 
# f.close()
  


# f=open("ext.txt","a",encoding="utf8")
# f.write("merhaba bu tamamen dosya içine append ile veri eklemek için oluşturuldu....")      #burada dikkat etmen gereken bir dosyayı aynı
#satirda hem yazıp hem okuyamazsın....


# with open("ext.txt","r") as f:
#     (f.read())
    

    #Dosya oluşturma


# a=open("program1.py","w",encoding="utf8")
# a.write("bu program python tarafından oto olarak oluşturuldu...")
# a.write("\na=input('bir kelime gir\t:')")
# a.write("\nprint(a*20)")
# a.write("\ninput()")

# # program1.py dosyasını oluştur ve içine Python kodlarını yaz
# with open("program1.py", "w", encoding="utf8") as a:
#     a.write("bu program python tarafından oto olarak oluşturuldu...\n")
#     a.write("a=input('bir kelime gir\t:')\n")
#     a.write("print(a*20)\n")
#     a.write("input()\n")

# print("program1.py dosyası başarıyla oluşturuldu!")

# d=open("dosya.txt","a",encoding=utf8) #aynı klasorde dosya aç
# d.write("merhaba\n") #dosya yaz
# d.close()      #dosyayı kapat
# print("dosya yazılıdı")

#Bir ust klasorde dosya oluşturma....

# d=open("../ust_klasor_dosyasi.txt","a",encoding="utf8")
# d.write("bu dosya bir üst klasore yazıldı\n")
# d.close()
# print("ust klasorde dosya yazıldı git kontrol et....")   

#belirli bir alt klasore dosya açma

# d=open("denemeKlasoru/denem.txt","a",encoding="utf8")
# d.write("Bu dosya alt klasorde açıldı\n")
# d.close()

#Konum belirterek dosya açma

# d=open("D:/Deneme/dosya.txt","a",encoding="utf8")
# d.write("bu dosya D dizininde Deneme klasoru açıılıp içine deneme.txt dosyası oluşturulacak")
# d.close()

# import os
# os.makedirs("D:/deneme2",exist_ok=True)


# klasor=input("klasor gir")
# dosya=input("dosya gir")

# tam_yol=f"{klasor}/{dosya}"



# d=open(tam_yol,"a",encoding="utf8")
# d.write("dostum hadi iyisin")
# d.close()

# osya_yolu = "E:/rehber.txt"

# with open(dosya_yolu, "r") as f:
#     satirlar = f.readlines()

# print("\n📄 DOSYA İÇERİĞİ 📄")
# print("════════════════════")

# a = 1
# for satir in satirlar:
#     print(f"{a}. satır: {satir.strip()}")
#     a += 1 


# a=open("rehber.txt","r+",encoding="utf8")
# while True:
#     b=input("dosyaya girilecek verileri yazın")          ##input ile deger alıp dosya içine yaziyor ama eski verileri siliyor....
#     if b=="q":
#         break
#     else:
#         a.writelines(b)
#         a.writelines("\n")
#     a.close


# with open("rehber.txt","a",encoding="utf8") as a:
#     while True:
#         b=input("dOSYAYA GİRİLECEK VERİLERİ YAZIN:")
#         if b.lower()=="q":               #buradan sonradan bak veri dosyaya yazılmıyor ama hatada vermiyor.....
#             break
#         else:
#             a.writelines(b)
#             a.writelines("\n")


# with open("rehber.txt","r+",encoding="utf8") as aptik:
#     aptik.seek(0,2)
#     while True:
#         b=input("Dosyaya girilecek verileri yazın:\t")
#         if b.lower()=="q":
#             break
#         else:
#             aptik.writelines(b+"\n")


# try:
#     f=open("ext3.txt","r",encoding="utf8")
#     print(f.read())
# except:
#     print("yazdıgın uygulama çalışmıyor boşuna deneme ve kimseyide yorma")


# try:
#     dosya=open("textted.txt","r")
    

#     a=1
#     for kayit in dosya.readlines():
#         print(f"{a}.{kayit.strip()}" )
#         a+=1


# except:
#     print("dosya bulunamadı")
#     input("devam etmek için entera basın")



# try:
#     f=open("textte.txt","r")
#     print(f.read())
# except:
#     print("dosya bulunamadı")
# finally:
#      print("işlem tamamlandı")

# try:
#     f = open("rehberr.txt", "r")
#     print(f.read())
# except FileNotFoundError:  # Eğer dosya bulunamazsa
#     print("⚠ Dosya bulunamadı, lütfen kontrol edin!")
# except PermissionError:  # Eğer izin hatası olursa
#     print("⚠ Dosya erişimi reddedildi, yetkiyi kontrol edin!")
# except Exception as e:  # Diğer tüm hatalar için
#     print(f"⚠ Beklenmeyen bir hata oluştu: {e}")

