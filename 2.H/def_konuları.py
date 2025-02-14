#****************TERNARY************************************



#print("xx") if 50 < 20 else print("yy")
# ort=50
# print("geçti") if ort > 50 else print("kaldı")


#DEF FONKSİYON KONULARI___________________________________________________________________________________

# def selamla ():
#   print("merhaba") 
#   print("nasılsın")           DEFINATİON BASİT FONKSİYON


# selamla()
# selamla()
# selamla()


# def topla():
#     print("toplam:", 5+5)


# topla()

# def topla(aa,bb):   #________________________parametre alan fonksiyon____________________________________
#     print("toplam", aa+bb)
# topla(5,4)

# def topla(k,l):
#     print("toplam", k+l)
# topla(3,3)

# def çift_tek(sayi):
#     if sayi % 2 == 0:
#         print(sayi,"çift")   ___________________PARAMETRE ALAN FONKSİYON___________________________
#     else:
#         print(sayi, "tek")

# çift_tek(1124)



# def karakter(metin):
#     sayac= len(metin)
#     print("vurayı ben yazıyoum",sayac)

# karakter("aptikdemir")


# def topla(aa,bb):
#     return f"toplam: {aa+bb}"
# print (topla(3,6))


# def carp (xx,yy):
#     return(xx*yy)
# print(carp(2,carp(2,6)))


# def topla(aa,bb):
#     return"toplam: aa+bb"  #string donderir
# print(topla(3,6))
                              


def topla(aa,bb):
    return f"toplam:{aa+bb}"
print(topla(3,5))