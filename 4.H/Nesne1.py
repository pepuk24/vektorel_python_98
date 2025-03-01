# 1. Sınıf Tanımlama
class Ilan:
    
    # 2. Özellikler Tanımlanıyor (Varsayılan Değerler)
    ilan_no = "_"
    ilan_adi = "_"
    ilan_aciklamasi = "_"

    # 3. Kurucu Metod (__init__)
    def __init__(self, a, b, c="_"):  # Açıklama opsiyonel hale getirildi
        self.ilan_no = a
        self.ilan_adi = b
        self.ilan_aciklamasi = c

    # 4. İlan Bilgilerini Gösteren Fonksiyon
    def ilan_bilgileri(self, uyelik_tipi):
        if uyelik_tipi == "premium":
            print("Merhaba çok değerli üyemiz")
            print(f"İlan adı: {self.ilan_adi}, \nİlan no: {self.ilan_no}")

        elif uyelik_tipi == "basic":
            print("Hoşgeldiniz sayın üyemiz")
            print(f"İlan adı: {self.ilan_adi}, İlan no: {self.ilan_no}")

# 5. İlan Nesneleri Oluşturma
ilan_1111 = Ilan("3333", "Araba")
ilan_222 = Ilan("5555", "Ev")

# 6. ilan_bilgileri Fonksiyonu Çağırma
ilan_1111.ilan_bilgileri("basic")
ilan_222.ilan_bilgileri("ilan_aciklamasi")
