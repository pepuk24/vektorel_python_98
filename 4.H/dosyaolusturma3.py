# # d=open("xxx.txt","a",encoding="utf-8") as xxx:
# #  dosya=xxx

# #  print(d.read)

# # d=open("deneme text.txt","a")  #PROJE DOSYASINDA ACAR DOSYAYI
# # d=open("../deneme text.txt","a") #Linuxda old gibi dosyayı bulunan konumdan 2 konum ileriye kaydeder....
# d=open("D:/deneme/deneme.text","a",encoding="utf-8")
# d.write("BURADAKİ BİLGİLER d:/DENEME/deneme.txt içine yazılacak")

# with open("dosya.txt","w" ) as d:
#     d.write("merhaba python")

# with open("C:/Users/aptik24/Desktop/dosya.txt","w") as d:
#     d.write("Masaustune kaydedildi...")


# import os 
# klasor="veriler"
# if not os.path.exists(klasor): #EGER KLASOR YOKSA OLUŞTUR
#   os.makedirs(klasor)

# with open(os.path.join(klasor, "dosya.txt"),  "w") as d:
#  d.write("dosya VERILER klasorune kaydedildi")

# with open("D:/DENEME/deneme.txt","w") as d:
#    d.write("D surucusune kaydedilmesi lazim")

# import os 
# dosya_yolu="D:/DENEME/deneme.txt"
# klasor=os.path.dirname(dosya_yolu) #Dosyanın bulundugu klasoru al...

# if not os.path.exists(klasor):
#     os.makedirs(klasor) #klasoru oluştur

# with open(dosya_yolu,"w",encoding="utf-8") as xxx:
#     xxx.write("bu dosya taa uzaklaredan D surucusunun içindeki deneme.txt dosyasına yazılacaktır")
