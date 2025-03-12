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

ilan1 = Ilan(123,"Deneme ilanı1")
ilan2 = EvIlan(124,"Deneme ilanı2",120)

ilan1.yaz()
ilan2.yaz()