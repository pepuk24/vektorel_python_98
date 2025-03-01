def ekle():
    """ Rehbere yeni kişi ekleme fonksiyonu """

    dosya = open("rehber.txt", "a")  # "a" append modunda aç, üzerine ekleme yap
    print("╔═════════════ REHBERE EKLEME ════════════════════════════╗")
    
    ad = input("║ Ad giriniz            : ")
    no = input("║ Numara giriniz        : ")
    card = input("║ Kredi kartı giriniz   : ")é

    dosya.write(f"İsim: {ad} | Tel No: {no} | Kredi Kartı: {card}\n")
    dosya.close()
    print("║ Bilgiler başarıyla eklendi! ║")
    print("╚══════════════════════════════════════════════════════╝")

def oku():
    """ Rehber dosyasını okuma fonksiyonu """
    try:
        with open("rehber.txt", "r") as dosya:  # Dosyayı güvenli şekilde aç
            okunan = dosya.read()
            print("\n╔══════════ REHBER İÇERİĞİ ══════════╗")
            print(okunan if okunan else "Rehber boş!")
            print("╚════════════════════════════════════╝")
    except FileNotFoundError:
        print("Hata: 'rehber.txt' bulunamadı. Önce ekleme yapın.")

# Fonksiyonları çağırmak için:
# ekle()  # Yeni kayıt eklemek için
# oku()   # Rehberi okumak için
ekle()