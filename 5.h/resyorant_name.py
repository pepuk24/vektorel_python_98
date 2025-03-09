class Restorant():
    def __init__(self,name,cuise_type):
        self.name=name
        self.cuise_type=cuise_type

    def descrip_restorant(self):
        print(f"{self.name} restoranı {self.cuise_type} yemegini veriyor... ")

    def open_restorant(self):
        print(f"{self.name} ismindeki restoranımız açıktir...")


restoran1=Restorant("Antep","sogan_kebabı")
restorant2=Restorant("Erzincan","Doner")
restorant3=Restorant("altınok","izmir_kofte")

# x=restoran1.name
# print(x)        
# xx=restoran1.cuise_type
# print(xx)

restoran1.descrip_restorant()
restoran1.open_restorant()


# z=restorant2.name
# zz=restorant3.name
# print(z,zz)

restoran1.descrip_restorant()
restorant2.descrip_restorant()
restorant3.descrip_restorant()


restoran1.open_restorant()
restorant2.open_restorant()
restorant3.open_restorant()