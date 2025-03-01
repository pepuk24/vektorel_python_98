# import os
# klasor="rehber_klasoru"

# if not os.path.exists(klasor):
#     os.makedirs(klasor)

 
#     for a in range(10):
#         dosya_yolu=f"{klasor}/rehber{a}.txt"
#         with open(dosya_yolu,"w") as dosya:
#             dosya.write("deneme1")


print("\n rehber klasor içerigi")



# #tum dosyalardaki verileri okuma 
# print ("\n rehber dosya içerigi")
# print("-----------------------------------")

# for a in range(10):
#     dosya_yolu=f"rehber_klasoru/rehber{a}.txt"
#     with open(dosya_yolu,"r",encoding="utf8") as dosya:
#         içerik=dosya.read()
#         print(f"{dosya_yolu} ile {içerik}")
        


with open("rehber_klasoru/sayilar.txt","w",encoding="utf8" ) as sayi_dosyasi:
    for i in range(1,101):
        sayi_dosyasi.write(f"{i}\n")
print("sayilar.txt içine 1 den 100 kadar sayilar yazilacak")