degisken = 11  # Global değişken

# def ornek():
#     global degisken
#     degisken=20
#     tplm=degisken+4
#     print("fonnksiyon içindeki toplam:",tplm)
#     return tplm
# tplm=ornek()
# print("fonksiyon dısşındaki toplam",tplm)
# print("onceki dış degişken",degisken)
# print("guncellenen dışarıdaki degişken",degisken)      #buna benzer yeni bir ornek çız konu ismi2 2. Fonksiyon İçinde Oluşturulan Değişkeni Fonksiyon Dışına Aktarmak







#3. global Kullanmadan Fonksiyon İçinde Global Değişkeni Kullanmak


# degişken=11
# def ornek():
  
#     toplam=degişken+4
#     print("fonksiyon içerisi",toplam)


# ornek()
# print("disarıdaki glabal degişken",degişken)




# def hesap():
#     degişken=10
#     sonuc=degişken*10
   
#     return sonuc
#     print(sonuc)     # ** Buradan neden çıktı alamıyorum 
   
# hesap()
# dıs_sonuc=hesap()

# print("içerdeki degeri dısaı atama",dıs_sonuc)

# def jur():
#     a=20
#     b=40
#     toplam=a+b
#     return toplam

# dar=jur()
# print(dar)

# jur()


# degisken = 11
# def fonksiyon1():
#     # print("Yereldeki1:",degisken) # atama yapılacaksa öncesinde değişken kullanılamaz
#     # global degisken
#     degisken = 22
#     print("Yereldeki2:",degisken)

# fonksiyon1()
# print("Globaldeki:",degisken)




# def dis_fonksiyon():
#     dis_degisken = 10  # Dış fonksiyonun değişkeni

#     def iç():
#         içd=20
#         print("iç de" ,içd)
#         print("dış" ,dis_degisken)
#     iç()
# dis_fonksiyon()

# degişken=20
# def hesap():
#     global degişken
#     degişken=degişken+6
#     print("fonksiyon içindeki degişken",degişken)
# hesap()
# print("guncellenen degişken",degişken)


# # Örnek-6:
# degişken=11
# def fonk():
#     global degişken
#     degişken=22
#     degişken=degişken+5
#     print("yereldeki",degişken)
#     return degişken
# degişken=fonk()

# print("dısardaki degisken",degişken)
# fonk()




# degisken = 11  # 🌍 ✅ GLOBAL DEĞİŞKEN (Tüm programda geçerli)

# def fonksiyon1():
#     global degisken
#     degisken=degisken + 22  # ❌ Yeni bir yerel (local) değişken oluşturuldu, global değişken değişmedi!
#     print("fonksiyon Yereldeki:", degisken)  # Çıktı: Yereldeki: 22
#     def ictekiFonksiyon():
        
#         degisken = 44  # ❌ Yeni bir yerel değişken daha oluşturuldu
#         print("İçteki fonksiyon:", degisken)  # Çıktı: İçteki fonksiyon: 33

    
#     ictekiFonksiyon()



# def fonksiyon1():
#     def ic_fonksiyon():
#         print("Bu iç fonksiyon!")

#     # ic_fonksiyon()  # İç fonksiyon burada çağrıldığı için zorunlu

# fonksiyon1()
# print("yarragım buda diş fonksiyon")


# degisken=11
# def fonksiyon1():
#     global degisken
#     degisken = 22
#     print("Yereldeki:",degisken)
#     def ictekiFonksiyon():
#         degisken = 33
#         print("İçteki fonksiyon:",degisken)
#     ictekiFonksiyon()

# fonksiyon1()
# print(degisken)


# degisken = 11
# def fonksiyon1():
#     global degisken # içtekinde global olunca bu önemini yitirir.
#     degisken = 22
#     print("Yereldeki:",degisken)
#     def ictekiFonksiyon():
#         global degisken
#         degisken = 33
#         print("İçteki fonksiyon:",degisken)
#     ictekiFonksiyon()

# fonksiyon1()
# print("Globaldeki:",degisken)


# # Soru-1
# x = 50
# def fonksiyon1(a):
#     global x
#     print("1.Durum=",a)
#     print("2.Durum=",x) # global x olduğundan x=.. dan önce kullanılabilir
#     x=100
#     print("3.Durum=",x)
# fonksiyon1(20)
# print("4.Durum=",x)

 


# counter = 10

# def increase():
#     global counter
#     for i in range(5):
       
#         print(counter)
#         counter -= 1

# increase()


# def dışarı(x):
#     def içeri(y):
#         return x+y
#     return içeri
# func=dışarı(10)
# print(func(5))
# print(func(20))



# def et(lst,element=0):
#     lst.append(element)
#     return lst
# list1=[]
# print(et(add.ele))


# def sleep_in(weekday, vacation):
#   if not weekday or vacation:
#     return True
#   else:
#     return False
#   # This can be shortened to: return(not weekday or vacation)
# sleep_in(vacation="saturday", weekday="friday")
# print(sleep_in(vacation="saturday", weekday="friday"))



# hava_guzel=True
# zaman_var=False

# if hava_guzel and zaman_var:
#   print("disari çık")
# else:
#   print("evde kalıyorum")


# mesaj = "merhaba"
# print(mesaj[0])
# print (len(mesaj))


# ad="ali"
# selam="merhaba"+ ad
# print(selam)


# def with_no(str):
#     return "no:" +str
# print(with_no("merhaba"))



nums=[1,2,3,4,5]
print(nums[4])