def anamenu():
    print("\033[34m                                                                      ")

    print("                               ╔══════════════════════════════════════════════╗")
    print("                               ║                                              ║")
    print("                               ║              UYGULAMALAR                     ║")
    print("                               ║                                              ║")
    print("                               ╚══════════════════════════════════════════════╝")

    print("                               ╔══════════════════════════════════════════════╗")
    print("                               ║                                              ║") 
    print("                               ║                                              ║")
    print("                               ║         1-MESAFE BİRİM ÖLÇÜMÜ                ║")
    print("                               ║                                              ║")
    print("                               ║         2-OYUNLAR                            ║")                             
    print("                               ║                                              ║")
    print("                               ║         3-TAKVİM                             ║")
    print("                               ║                                              ║") 
    print("                               ║         4-DÖVİZ UYGULAMASI                   ║") 
    print("                               ║                                              ║") 
    print("                               ║         5-Çıkış                              ║")
    print("                               ║                                              ║")
    print("                               ║          SEÇİMİNİ YAP!!                      ║")
    print("                               ╚══════════════════════════════════════════════╝")

    secim = input("Seçim yapınız: ")

    if secim == "1":
        hmenu()
    elif secim == "2":
        oyunlar()
    elif secim == "3":
        takvim()
    elif secim == "4":
        doviz()
    elif secim == "5":
        print("Çıkış yapılıyor...")
        exit()
    else:
        print("Geçersiz bir giriş yaptınız..")
        anamenu()  # Tekrar ana menüye dön

def hmenu():
    print("\033[34m                                                                      ")
    print("                               ╔══════════════════════════════════════════════╗")
    print("                               ║                                              ║")
    print("                               ║             MESAFE ÇEVİRİCİ                  ║")
    print("                               ║                                              ║")
    print("                               ╚══════════════════════════════════════════════╝")

    print("                               ╔══════════════════════════════════════════════╗")
    print("                               ║                                              ║") 
    print("                               ║                                              ║")
    print("                               ║         1-METRE ==> KİLOMETRE                ║")
    print("                               ║         2-KM    ==> METRE                    ║")
    print("                               ║         3-METRE ==> İNÇ                      ║")
    print("                               ║         4-İNÇ   ==> METRE                    ║")                             
    print("                               ║         5-KM    ==> MİL                      ║")
    print("                               ║         6-MİL   ==> KİLOMETRE                ║")
    print("                               ║         7-FEET  ==> KİLOMETRE                ║") 
    print("                               ║         8-KM    ==> FEET                     ║") 
    print("                               ║         9-YARD  ==> KİLOMETRE                ║") 
    print("                               ║         10-KM   ==> YARD                     ║")
    print("                               ║                                              ║")
    print("                               ║             SEÇİMİNİ YAP!!                   ║")
    print("                               ╚══════════════════════════════════════════════╝")

    secim = input("Seçim yapınız: ")

    if secim == "1":
        print("Metre -> Kilometre seçildi!")
    elif secim == "2":
        print("Kilometre -> Metre seçildi!")
    elif secim == "3":
        print("Metre -> İnç seçildi!")
    elif secim == "4":
        print("İnç -> Metre seçildi!")
    elif secim == "5":
        print("Kilometre -> Mil seçildi!")
    elif secim == "6":
        print("Mil -> Kilometre seçildi!")
    elif secim == "7":
        print("Feet -> Kilometre seçildi!")
    elif secim == "8":
        print("Kilometre -> Feet seçildi!")
    elif secim == "9":
        print("Yard -> Kilometre seçildi!")
    elif secim == "10":
        print("Kilometre -> Yard seçildi!")
    else:
        print("Geçersiz seçim! Tekrar deneyin.")

    anamenu()  # İşlem bitince ana menüye dön

def oyunlar():
    print("Bu menü henüz hazır değil.")
    input("Ana menüye dönmek için Enter'a basın...")
    anamenu()  # Oyun menüsünden çıkınca tekrar ana menüye dön

def takvim():
    print("Takvim uygulaması çalıştırılıyor...")
    input("Ana menüye dönmek için Enter'a basın...")
    anamenu()

def doviz():
    print("Döviz uygulaması çalıştırılıyor...")
    input("Ana menüye dönmek için Enter'a basın...")
    anamenu()

anamenu()  # Program başlatıldığında ilk olarak ana menü açılacak