class Ilan():
    def __init__(self,iln,bas):
        self.ilan_num = iln
        self.ilan_baslik = bas
    def yaz(self):
        print("Ilan bilgileri:",self.ilan_baslik, self.ilan_num)

class EvIlan(Ilan):
    def __init__(self,ilannum, baslik, metrek):
        self.metrekare = metrek
        super().__init__(ilannum, baslik)
    def yaz(self):
        print("Ev ilanı bilgileri:",self.ilan_baslik, self.ilan_num, self.metrekare)
class KiralikEv(EvIlan):
    def __init__(self,ilannum, baslik, metrek, dep):
        self.depozito = dep
        super().__init__(ilannum, baslik,metrek)
    def yaz(self):
        print("Kiralık ev ilanı bilgileri:",self.ilan_baslik, self.ilan_num, self.metrekare,"Depozit:",self.depozito)

ilan1 = Ilan(123,"Deneme ilanı1")
ilan2 = EvIlan(124,"Deneme ilanı2",120)
ilan3 = KiralikEv(125,"Deneme başlık3",135,5000)

ilan1.yaz()
ilan2.yaz()
ilan3.yaz()