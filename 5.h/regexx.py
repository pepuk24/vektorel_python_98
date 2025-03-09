import re
# ornek="merhaba dostum en sevdigim kod base42"
# pattern="base\d\d"
# k=re.search(pattern,ornek)
cumle='selam ,benim telefon numaram 0535-4564218'
# print(k)
# print(len(ornek))
# print(type(k))

patern=r"\d\d\d\d-\d\d\d\d\d\d\d"
k=re.search(patern,cumle)
print(k)
print(type(k))
print(len(cumle))