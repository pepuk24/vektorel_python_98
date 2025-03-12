class BankaKasasi():
    __KasadakiMiktar = 0 # __ ile kapsüllenmiş bilgi
    def kasadakiMiktar(self):
        return self.__KasadakiMiktar
   
    def kasayaParaEkle(self, miktar):
        self.__KasadakiMiktar += miktar

    def kasadanParaCikar(self,miktar):
        self.__KasadakiMiktar += miktar

class BankaMusterisi():

    adiSoyadi = "---"
    hesapNumarasi = "tanımlanmamış" # public yada global
    __kalanParasi = 0 # __ ile kapsüllenmiş bilgi. Private özellik/propery.
    __musteriLimiti = 10000
    # private özellikler sınıf dışından değiştirilemez.
    # sınıf içerisindeki bir fonksiyon aracılığıyla değişir.
    def __init__(self,ad,no,para):
        self.adiSoyadi = ad
        self.hesapNumarasi = no
        # self.__kalanParasi = para
    def paraCek(self,cekilen):
        self.__kalanParasi -= cekilen
        # kasa1.__KasadakiMiktar -= cekilen
        kasa1.kasadanParaCikar(cekilen)
   
    def paraYatir(self,yatirilan):
        self.__kalanParasi += yatirilan
        # kasa1.__KasadakiMiktar += yatirilan
        kasa1.kasayaParaEkle(yatirilan)
   
    def kalanParaMiktariniGoster(self):
        return self.__kalanParasi
    
    def limitArtir(self,talepEdilenLimit,device):
        if device == "Mobil":
            if self.musteriKrediNotuOgren() > 1000:
                if talepEdilenLimit<50000:
                    self.__musteriLimiti = talepEdilenLimit
                    print(f"Limitiniz {talepEdilenLimit} olarak güncellendi.")
                else : 
                    print("50000 TL üzeri limit artışı yapılamamaktadır.")
            else:
                print("Kredi notunuz düşük, limit artış t olumsuz.")
        else:
            print("Limit artışı sadece mobilden yapılır.")

    def musteriKrediNotuOgren(self ):
        if self.hesapNumarasi == "45745874514": return 1500
        if self.hesapNumarasi == "22222222222": return 900
    
    def musteriBorcuOgren(self ):
        if self.hesapNumarasi == "45745874514": return 25000
        if self.hesapNumarasi == "22222222222": return 2000
    def musteriLimitiOgren(self):
        return self.__musteriLimiti-self.musteriBorcuOgren()

kasa1 = BankaKasasi()
kasa1.KasadaKalanMiktar = 50000

musteri1 = BankaMusterisi("Nurdan KARA","45745874514",5000)

print(f"\n\nKasada kalan para miktarı : {kasa1.KasadaKalanMiktar}")

print(f"\n\nMüşteri Bilgileri\n\
    Adı: \t{musteri1.adiSoyadi}\n\
    Hesap No : \t{musteri1.hesapNumarasi}\n")

musteri1.adiSoyadi = "Ali AK"
# musteri1.__kalanParasi += 5000
musteri1.paraYatir(5000)

print(f"\n\nKasada kalan para miktarı : {kasa1.KasadaKalanMiktar}")

print(f"\n\nMüşteri Bilgileri\n\
    Adı: \t{musteri1.adiSoyadi}\n\
    Hesap No : \t{musteri1.hesapNumarasi}\n")

print("Müşteri1 kalan parası:", musteri1.kalanParaMiktariniGoster())
print("Kasadaki miktar:", kasa1.kasadakiMiktar())

musteri1.paraYatir(20)
print("Müşteri1 kalan parası:", musteri1.kalanParaMiktariniGoster())
print("Kasadaki miktar:", kasa1.kasadakiMiktar())

musteri2 = BankaMusterisi("Ebru SARICAOĞLU","524785",6000)
musteri2.paraYatir(1000)
print("Müşteri1 kalan parası:", musteri1.kalanParaMiktariniGoster())
print("Müşteri2 kalan parası:", musteri2.kalanParaMiktariniGoster())
print("Kasadaki miktar:", kasa1.kasadakiMiktar())

musteri2.paraYatir(3)
print("Müşteri1 kalan parası:", musteri1.kalanParaMiktariniGoster())
print("Müşteri2 kalan parası:", musteri2.kalanParaMiktariniGoster())
print("Kasadaki miktar:", kasa1.kasadakiMiktar())

# print(musteri1.__musteriLimiti)
musteri1.limitArtir(30000,"Mobil")
print("Kalan limit:",musteri1.musteriLimitiOgren())
