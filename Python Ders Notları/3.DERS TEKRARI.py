                                                      #ÇIKTILAR

print (542)      #                                     ==> 542
print (542+3)   #                                      ==> 545
print ("542+3") # Stringdir...                         ==> 542+3
#print (vektorel)   # Hata verir.....



a=5
print(a) #Degiskenler tirnaksiz yazillir....            ==>  5

a=555
print("a") #Stringdir.                                  ==>   a

print('Erenin annesi "gel" dedi.')
print ('Eren\'in annesi "gel" dedi')     # \ isareti ' karmasasini ortadan kaldirir...

                                          # ==> Erenin annesi "gel" dedi.
                                          # ==> Eren'in annesi "gel" dedi       
print('''Eren'in annesi "gel" dedi.''')   # ==> Eren'in annesi "gel" dedi.




#\n alt satira gecer , \t  tab yapar.........

print ("Python \t\togrenme \tkursu...")      # ==> Python 		ogrenme 	kursu...
print ("Python \nogrenme \nkursu...")        #==> pthon
                                             #         ogrenme
                                             #                  kursu...


print("\t\tOgrenci Bilgileri\n\t\t====================")  #===>             Ogrenci Bilgileri
		                                                #          ====================   
print ("\tAdi\t:\n\tSoyadi\t: \n\tNumarasi:")                 #              Adi:
	                                                     #            Soyadi: 
	                                                   #            Numarasi:



x=5
print("x degeri=" , x)         #  ===>   x degeri=5

#  print=("x degeri=" , X)    Hata verir Python buyuk-kucuk harflere duyarlidir...Dikkat buradaki X buyuk....
print ("============================================================")

Adi="Remzi"
Soyadi="Demir"
No=444
print("\t\tOgrenci Bilgileri\n\t\t=================================")
		                                             
print ("\tAdi\t:",Adi," \n\tSoyadi\t: ",Soyadi," \n\tNumarasi: " ,No )   # ==> Degiskenlerin arasina , koymak gerekiyor


#BIR FONKSIYONUN ICINDE BASKA BIR FONKSOYON KULLANILABILIR......
print("============================================================")

abc=4
dfg="ORNEKLEMELER"
hkl= len ("ORNEKLEMELER")   # ====> len string uzunlugunu yazar konsola......

print(abc)                 #  =====> 4
print(dfg)                 #  =====> ORNEKLEMELER
print(hkl)                 #  =====>  12
print (len ("REMZIDEMIR")) #  =====>  10

print("=============================================================")

a=10
b=20                             
c=str(a)                   # (str) sayisal ifadeyi stringe çevirir....                    
d=str(b)
print(a+b)       #   ======>    30


print (10+20)                   #  ====>    30
print("10"+"20")                #  ======>  1020   Dikkat edersen STRING dir....
print (c+d)                     #  =====>  1020   Yukarida dikkat edersen degiskenlerin basinde (str) var yani sayilari string olarak ele aliyor...
print (str(3)+ str(5))          #  =====>  35  (str) olduguu icin rakamlari stringe ceviriyor.....

print (len(str(3)+ str (5)))    #  =====>  2 (len) karekter olarak ele aldigi için 35 iki karakter olarak gorur...

"""
Buradaki
         yazilanlar üç noktanin
            yorumlayici oldugunu
                 gostermek icin yapilmistir...
                    Cok satirli Yorumlama...
   Tek satirlik yorumlamalarda # kullanildigini UNUTMA!!!
                                                           """
print ("============================================================")
 #PRINT F ILE METIN SEKILLENDIRME================================╗

Ad="Remzi"
Soyadi="Demir"
No=444
print("Name\t:" ,Ad, "\nSurname\t:" ,Soyadi, "\nNumber\t:" ,No)

print("==============================================================")

Ad="Remzi"
Soyadi="Demir"
No=444

sonuc=f"Nav\t: {Ad} \nPeshnav\t:{Soyadi}\nNomar\t:{No}"
print(sonuc)


print("==============================================================")
# Yada seklinde yazilir.........................................................
Ad="Remzi"
Soyadi="Demir"
No=444
print(f"Ad\t:{Adi}\nSoyadi\t:{Soyadi}\nNumara\t:{No}")




print("=============================================================================")
'''
ad=input()
sa=input()

print (f"Girdiginiz kullanicinin Adi {ad}, ve soyadi {sa}, sistemde gozukmuyor...")
print("==============================================================================")
ad= input ("Adi\t:")
soyadi= input ("Soyadi\t:")
print(f" Girdiginiz bilgiler sistemde gozukmuyor",{ad},{soyadi})
Tirnaklari kaldirarak deneyebilirsiniz.....
'''


input()
