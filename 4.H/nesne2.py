# class Araba:
#     def __init__(self, marka, model, renk,hiz):
#         self.marka = marka
#         self.model = model
#         self.renk = renk
#         self.hiz=hiz



#     def calistir(self):
#         print(f"{self.marka} {self.model} çalıştırıldı...")

#     def dur(self):
#         print(f"{self.marka} {self.model} durdu...")

# # Nesne oluştur
# araba1 = Araba("Toyota", "Corolla", "Kırmızı")

# # Metotları çağır
# araba1.calistir()  # Çıktı: Toyota Corolla çalıştırıldı...
# araba1.dur()       # Çıktı: Toyota Corolla durdu...
# araba2=Araba("bmw","m5","sari")             
# def hizlan(self,artis):
#     self.hiz+=artis
#     print(f"{self.marka}{self.model} hizlandı.şu anki hızı {self.hiz}")


# class Araba:
#     def __init__(self, marka, model, yil):
#         self.marka = marka  # Markasını sakla
#         self.model = model  # Modelini sakla
#         self.yil = yil  # Üretim yılını sakla

# # Şimdi nesne oluşturalım
# araba1 = Araba("Toyota", "Corolla", 2022)
# araba2 = Araba("BMW", "M5", 2023)

# print(araba1.marka, araba1.model, araba1.yil)  # Toyota Corolla 2022
# print(araba2.marka, araba2.model, araba2.yil)  # BMW M5 2023


class Araba():
    def __init__(self,marka,model,yil,hiz=0):
        self.marka=marka
        self.model=model
        self.yil=yil
        self.hiz=hiz

    def hizlan(self,artis):
        self.hiz+=artis
        print(f"{self.marka} {self.model} {self.hiz} km/h hizla gidiyor...")
        

    def fren_yap(self):
        self.hiz=0
        print(f"{self.marka} {self.model} durdu...") 

    def __str__(self):
        return f"{self.yil} Model {self.marka} {self.model} şu anki hizi {self.hiz}" 


araba1=Araba("sahin","a3",2000)

print(araba1)
araba1.hizlan(30)
print(araba1)