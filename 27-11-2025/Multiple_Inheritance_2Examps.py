# Child inherits from multiple parents
# SmartPhone ← Camera + Phone

class Phone:
    def __init__(self,model,color,make):
        self.model=model
        self.color=color
        self.make=make
    def display(self):
        print("Model:",self.model," Color:",self.color," Make:",self.make)

class Camera:
    def __init__(self,brand,megapixels):
        self.brand=brand
        self.megapixels=megapixels
    def display(self):
        print("Brand:",self.brand,"Megapixels:",self.megapixels)

class Smartphone(Phone,Camera):
    def __init__(self,model,color,make,brand,megapixels):
        Phone.__init__(self,model,color,make)
        Camera.__init__(self,brand,megapixels)

    def display(self):
        print("Model:",self.model," Color:",self.color," Make:",self.make)
        print("Camera Megapixels:",self.megapixels)

P1=Phone(2020,"Red","Mica")
P1.display()
print()
C1=Camera("Nikon",20)
C1.display()
print()
S1=Smartphone(2020,"Red","Mica","Nikon",20)
S1.display()

