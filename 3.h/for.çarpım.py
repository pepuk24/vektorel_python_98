# for a in range (1,11):
#     print(a,"x")
#     print("-----------------------------")
#     for b in range (1,11):
#          print(a,"x",b)



# for vv in range(20,50,7):
#     print(vv)
  
#     print("vv")

# STRİNG VE LİSTE İLE FOR KULLANIMI:::::
 
# for i in "aptik":
#    print(i,end="&")

ogrenciler=["ahmet" ,"mehmet","hakan"]
# for i in ogrenciler:
#     print(i)



# for x,e in enumerate(ogrenciler):
#     print(e,x)

#Liste doldurma

# ab=[i for i in range(10,30,3)]
# print(ab)

# print([i for i in "DENEME"])


# print(b*3 for b in "aptik")                             
# liste1=[[1,2,3],[4,5,6],[7,8,9]]
# liste2=[j for i in liste1 for j in i]      #  < ---
# print(liste2)                              #       |
#                                            #       |
# #for ile yapılışı                          #       |      ALTERNATİF FOR DONGUSU.....
#                                            #       |
# liste2=[]                                  #       |             Boş bir liste oluşturuyoruz
# for i in liste1:                           #  <----              liste1'in içindeki her alt listeyi al..
#     for j in i:                            #                     O alt listenin içindeki her elemanı al
#         liste2.append(j)                   #                     liste2'ye ekle
# print(liste2)                              #

#_____________________________________________________________________________________________________________________________________
# seker_kutusu=[maviSeker,kirmiziSeker],[yesilSeker,sariSeker]

# duzeltilmis=[seker for paket in seker_kutusu for seker in paket]
# print(duzeltilmis)


# duzeltilmis=[]
# for paket in seker_kutusu:
#     for seker in paket:
#         duzeltilmis.append(seker)
# print(duzeltilmis)

#_____________________________________________________________________________________________________________________________________



# sayi_list=[1,2,3,4,5,6,7,8,9]

# print([sayi*2 for sayi in sayi_list if sayi if sayi%2==0])


# FOR İLE BASİT ÇARPIM TABLOSU.....

for i in range(1,11):  
    print("\n", i, "ler basamağı")  
    print("------------------------------")  
    for b in range(1,11):  
        print(i, "x", b, "=", i * b)  



        
