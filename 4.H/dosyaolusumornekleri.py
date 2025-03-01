# dosya=open("ext.txt","r")
# satirlar=dosya.readlines()
# print(satirlar)


# a=1
# for kayit in dosya.readlines():
#     print(f"{a}.{kayit.strip()}")
#     a+=1

# dosya=open("rehber.txt","a")
# for a in range (9):
#     dosya.write(str(a)+"\n")
#     b=dosya.write(str(a)+"\n")
#     print(type(b))


# dosya=open("deneme.txt","w")
# for a in range(9):
#     dosya.write(str(a))
   


ad = input("Adınız nedir?")
dosya = open("Merhaba"+ad+".py","w")
yazilacakbilgi = 'print("Merhaba "+ad+"\\nBu python programi virusler gibi otomatik olusturuldu.")\ninput()'
dosya.write('print("Merhaba '+ad+'\\nBu python programi virusler gibi otomatik olusturuldu.")\ninput()')

