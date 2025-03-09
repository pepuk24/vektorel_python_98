class Hayvan():
    def ses_cikar(self):
        pass #alt sınıflar bunu kendileri tanimlayacak

class Kedi(Hayvan):
        def ses_cikar(self):
            return "Miyav"
        
class Kopek(Hayvan):
        def ses_cikar(self):
            return "Havvvv"
        
class Kuş(Hayvan):
        def ses_cikar(self):
            return "Qirik qirik"
        
hayvanlar=[Kedi(),Kopek(),Kuş()]

for xeyvan in hayvanlar:
      print(xeyvan.ses_cikar())

      print("---------------------------------------------")


print(FİLO)