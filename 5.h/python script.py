class Araba():
    def __init__(self,renk,model,marka):
        self.renk=renk
        self.model=model
        self.marka=marka

    def haraket(self):
        print(f"{self.marka} {self.model} hareket ediyor") 


araba1=Araba("kırmızı","civik","honda")

print(f"araba rengi {araba1.renk}")
print(f"araba markası {araba1.marka}")


