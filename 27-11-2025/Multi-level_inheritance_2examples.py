#Grandparent-Parent-Child
class Device:
    def __init__(self,device,year):
        self.device=device
        self.year=year

class Computer(Device):
    def __init__(self,device,year,os,warranty):
        super().__init__(device,year)
        self.os=os
        self.warranty=warranty
    def display(self):
        print("Device: ",self.device)
        print("Year: ",self.year)
        print("OS: ",self.os)
        print("Warranty: ",self.warranty)
class Laptop(Computer):
    def __init__(self,device,year,os,warranty,camera,microphone):
        super().__init__(device,year,os,warranty)
        self.camera=camera
        self.microphone=microphone

    def display(self):
        print("Device: ",self.device)
        print("Year: ",self.year)
        print("OS: ",self.os)
        print("Warranty: ",self.warranty)
        print("Camera present: ",self.camera)
        print("Mic present: ",self.microphone)

C1=Computer("Computer","2025","Windows",2030)
L1=Laptop("Laptop","2025","Windows",2030,"Yes","Yes")
L1.display()
print()
C1.display()
print()

class Animal:
    def __init__(self,animal,age):
        self.animal=animal
        self.age=age
    def display(self):
        print("Animal: ",self.animal)
        print("Age: ",self.age)

class Mammal(Animal):
    def __init__(self,animal,age,domesticOrWild):
        super().__init__(animal,age)
        self.domesticOrWild=domesticOrWild
    def display(self):
        print("Mammal: Yes" if self.animal=="Mammal" else "No")
        print("Age: ",self.age)
        print("Domestic Or Wild: ",self.domesticOrWild)

class Dog(Mammal):
    def __init__(self,animal,age,domesticOrWild,name):
        super().__init__(animal,age,domesticOrWild)
        self.name=name
    def display(self):
        print("Mammal: Yes" if self.animal == "Mammal" else "No")
        print("Age: ", self.age)
        print("Domestic Or Wild: ", self.domesticOrWild)
        print("Name: ", self.name)

A1=Animal("Mammal",20)
A1.display()
print()
M1=Mammal("Mammal",20,"Domestic")
M1.display()
print()
D1=Dog("Mammal",20,"Domestic","Bruno")
D1.display()