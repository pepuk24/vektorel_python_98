class Ogrenci:
    def __init__(self,xx,yy,zz="Normal"):
        self._ad = xx # public / her sınıfa, her yere açık
        self.no = yy
        self.__sd = zz # private/dışarıdan ulaşılamayan değişken.
        # Sadece kendi sınıfının içindeki metodlar ile ulaşılabilir.
   
    def saglikDurumu(self):
        return self.__sd
    def saglikDurumuAta(self,gelensd):
        self.__sd = gelensd

class LiseOgrenci(Ogrenci):
    def __init__(self, xx, yy, zz="Normal"):
        super().__init__(xx, yy, zz)
    def sdg(self):
        return self.__sd
    
    def sda(self,aa):
        self.__sd = aa


ogrenci1 = Ogrenci("Murat",698)
ogrenci2 = Ogrenci("Dila",741,"Astımı var") # Nesneye veri set etme
# print(ogrenci2.saglikDurumu()) # sd (sağlık durumu) nu okumak için method kullan.
# ogrenci1.__sd="Şeker var"  # Olmaz
print(ogrenci1._ad)
# print(ogrenci1.__sd) # Olmaz
# ogrenci1.__sd = "xxx"
ogrenci1._ad = "xxx"
ogrenci1.saglikDurumuAta("xxxx")
print(ogrenci1.saglikDurumu())
print(ogrenci1._ad)
# print(ogrenci1.saglikDurumu()) 

ogrenci4 = LiseOgrenci("aaaa",234)
ogrenci4.sda("eee")
print(ogrenci4.sdg())