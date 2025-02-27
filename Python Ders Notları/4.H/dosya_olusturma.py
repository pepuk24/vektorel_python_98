def ekle():

# open("rehber.txt","w")  #"w" ile yazılanların uzerine tekrardan yazı yazabilirizzzz....
# for a in range(10):
#    open(f"rehber{a}.txt","w")

# open("rehber.txt","w").write("merhaba") #dosya açma parametredsi olmadıgında açar
# open("rehber.txt","w").write("nasilsin")


dosya=open("rehber.txt","w")
dosya.write("merhaba dostum bugun durumun nasil")


  dosya=open("deneme.txt","a") #Appand özelligiyle yeni dosya oluşturabiliriz.....


# dosya.write("\n  3 satir ile devam ediliyor ve yeni eklemeler yapiliyor...")


#rehbere veri ekleme


print(" ╔═════════════REHBERE EKLEME══════════════════════════════╗     ")
print( "║ Ad giriniz                                          ║          " ,end="")   ; ad=input()              
print(" ║ Numara giriniz\t:                                       ║ " ,end="") ;        no=input()  
print(" ║ Kredi card:                                             ║   ",end="")  ; card=input()

dosya.write(f"isim===>{ad}tel no====>{no} kredi carti=====>{card}\n")
dosya.close()   #Close kullnılmaz ise dosya sorun çıkartabilir...


#BİLGİ OKUMA

def oku():
    dosya=("deneme.txt","r") #açma modu arg olmazsa defaul olrak "r" gelir...dosya=open("rehber.txt") ile aynı mantıktadır....
    okunan=dosya.read()

    print(okunan)
oku()



open("deneme.txt","r")