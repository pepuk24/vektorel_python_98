class Users():
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname

    def eric_descrip(self):
        print(f"{self.name} {self.surname}")
    def greet_user(self):
        print(f"Hi {self.name} thanks for your bible of Python")


user1=Users("erich","mathes")
user2=Users("Aptik","demir")


# x=user1.name
# z=user1.surname
# print(x,z)
# user1.eric_descrip()
# user1.greet_user()
user2.greet_user()
user2.eric_descrip()