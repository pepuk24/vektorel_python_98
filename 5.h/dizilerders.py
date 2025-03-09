def fonksiyon(**x):
    print(x)
    print(type(x))
    for s in x.items():
        print(s)

fonksiyon(adı="ali",soyadı="veli",yas=22)




def displayUser(**args):
    print(type(args))
    for key, value in args.items():
        print('{} => {}'.format(key, value))
displayUser(name='John', age=22, city='New York',ulke="turkiye")

# print((lambda x:x+2)(5))


def kareal(a):
    return a**2
print(kareal(5))


def kareal ():
    return a**2
