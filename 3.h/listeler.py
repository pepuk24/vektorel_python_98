# meyveler=["muz","dut","nar"]

# print(meyveler[1])

# print[] boş donderir

# meyverler2=["elma","armut"]
# print(meyverler2)

# print(meyverler2+meyveler)


# print(meyveler)


# meyverler2 += meyveler
# # print(meyverler2)

# meyverler2.append("kiwi")
# # print("B2:",meyverler2)

# meyverler2.insert(3,"kavun")
# # print("B3:",meyverler2)


# meyverler2.pop(5)
# print("B4:",meyverler2)



#TUPLE TANIMLAMA

meyveler=("muz","dut","nar")        #tuple(demet)
# print(meyveler)

meyveler2=["elma","armut"]     #list
# print(meyveler2)


# print(type(meyveler2))
# print(type(meyveler))


# print(meyveler2[1])
# print(meyveler[1])


#DİCTİONARY ÖRNEKLERİ.....

#key---value


# ogrenci={
#     "ad": "ahmet",
#     "no":   "123",
#     "sinif": "10a"
# }



# ogrenci_bilgileri={
# "ogrenci"   {
#     "ogrenci_adi" "remzi demir",
#     "ogrenci_no"  "222",
# }   ,

# "ogrenci2":{

# }


    

# }

kitap = {
    "ad": "1984",
    "yazar": "George Orwell",
    "yayin_yili": 1949
}

# print(kitap)

# print("İsmi:",kitap["ad"])

kitap["sayfa_sayisi"]=222
# print(kitap)

kitap["Yayin_evi"]="Kirmizi_kitap"
# print(kitap)



# print(kitap.keys())


# print(kitap.values())


# print(kitap.items())


ogrenci_bilgileri = {
    "ogrenci1": {
        "ogrenci_adi": "Remzi Demir",
        "ogrenci_no": "351"
    },
    "ogrenci2": {
        "ogrenci_adi": "Kemal KUTLU",
        "ogrenci_no": "458"
    }
}



# print(ogrenci_bilgileri)
# print("xx1:",ogrenci_bilgileri["ogrenci1"])


# print("xx2", ogrenci_bilgileri["ogrenci1"]["ogrenci_no"])


#eleman ekleme ve silme



ogrenci_bilgileri["ogrenci3"]={"ogrenci_adi": "Ayşe YILMAZ","ogrenci_no": "121"}
# print(ogrenci_bilgileri)

#Bİr elemanı silmek

del ogrenci_bilgileri["ogrenci2"]
# print(ogrenci_bilgileri)


#KEYLERİ LİSTELEMEK


# print(ogrenci_bilgileri.keys)


# print(ogrenci_bilgileri.values())

# print(ogrenci_bilgileri.items())

#STRİNGLER


aa="vektorel"
# print(aa)
# print(aa[0])
# print(aa[3:])

# print(aa[:3])
# print(aa[2:4])

# print(aa[2:8:2])


# for x in range(len(aa) +1):
#     print(aa[x:])

# aa = "Vektörel"
# print(len(aa))

urunler = ["Süt", "Ekmek", "Peynir"]
fiyatlar = [10, 5, 30]
# print(len(urunler))

# urun="ekmek"
# print(len(urun))

# for i in range(len(urunler)):
#     print(f"{urunler[i]}-{fiyatlar[i]} TL")




# aa="vektorel"
# aa[:x] ve aa[::-1] 


#STRİNG FUNCTİONLAR....
# print ("apTİK dEmİr".capitalize())

# print("APtik dEmir".lower())

# print("apTiK DeMir".upper())

# print("aPtİk dEMİR".title())
# print("Aptik demir".replace("a","e"))

# print("aptikdemir".count("i"))

# print("aptik demir".find("t"))

# ad=input("ad gir\t:")
# duz=ad.capitalize()
# print(f"hoş geldin {duz}")


# kufur="sen tam bir oruspu çocugusun"
# kufur=kufur.replace("oruspu", "*****")           # çıktı====> sen tam bir ***** çocugusun
# print(kufur)


# paragraf = "Python harika! Python öğrenmek çok eğlenceli, python ile neler yapılmaz ki..."
# print(paragraf.lower().count("python"))