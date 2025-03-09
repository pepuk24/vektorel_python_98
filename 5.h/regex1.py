import re
# cumle="Selam,benim telefon numaram 42base"

# # patern=r"\d{3,4}-\d{7}"
# patern=r"\d?"
# patern=r"\w+\d+"
# for eslesme in re.finditer(patern,cumle):
    


#     print("------------pattern çıktı---------------------")
#     print(eslesme.group(), eslesme.span())
#     print("---------------------len karekteri aşagıda----------------------")
#     print(len(cumle))
#     print("--------------type--------------------------")
#     print(type(patern))



import re

def gsm(tel_no):
    patern = r"(\d{3,4})(\d{7})"  # Burada - kaldırıldı çünkü girişte "-" yok
    eslesme = re.search(patern, tel_no)

    if eslesme:
        return eslesme.group(2)  # İlk gruptaki alan kodunu döndür
    else:
        return "Eşleşme bulunamadı"

tel_no = "05340502727"
print(gsm(tel_no))  # Çıktı: 0534