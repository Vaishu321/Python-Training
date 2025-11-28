# One parent → multiple child classes
# Vehicle → Car, Bike, Truck
# Employee → Manager, Developer, Tester

class Vehicle:
    def __init__(self,make,model,color,year):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
    def display(self):
        print("Make:",self.make,"Model:",self.model,"Year:",self.year)

class Car(Vehicle):
    def __init__(self,make,model,color,year,wheels,mileage):
        Vehicle.__init__(self,make,model,color,year)
        self.wheels = wheels
        self.mileage = mileage
    def display(self):
        print("Car:",self.make,"Model:",self.model,"Color: ",self.color,"Year:",self.year,"No. of Wheels:",self.wheels,"Mileage:",self.mileage)
class Bike(Vehicle):
    def __init__(self,make,model,color,year,wheels,engine):
        Vehicle.__init__(self,make,model,color,year)
        self.wheels = wheels
        self.engine = engine
    def display(self):
        print("Bike: ",self.make,"Model:",self.model,"Color: ",self.color,"Year:",self.year,"No. of Wheels:",self.wheels,"Engine:",self.engine)

b1=Bike("Metal",202,"black",2002,2,"1000maH")
C1=Car("Metal",202,"black",2002,2,"100km")
b1.display()
C1.display()
