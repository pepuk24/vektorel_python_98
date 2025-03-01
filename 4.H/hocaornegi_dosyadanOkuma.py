d=open("hocadosya.txt")
okunan=d.readlines()
# print(type(okunan))
for x in okunan:
    # print(type(x))

    x.split("|") #listeyi sag ve sol diye bolmek

    z=x.split("|")
    # print(type(z))

    print(z[0])