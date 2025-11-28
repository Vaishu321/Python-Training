#Parent-child
class Company:
    def __init__(self,name,age,joiningDate):
        self.name=name
        self.age=age
        self.joiningDate=joiningDate

class Employee(Company):
    def __init__(self,name,age,joiningDate,dept):
        super().__init__(name,age,joiningDate)
        self.dept=dept

E1=Employee('Emil',35,'2-9-2020',"IT")
print("Name: ",E1.name,"Age: ",E1.age,"Joining Date: ",E1.joiningDate,"Department: ",E1.dept)

class Vehicle:
    def __init__(self,type):
        self.type=type

class Car(Vehicle):
    def __init__(self,type,brand,model,year):
        super().__init__(type)
        self.brand=brand
        self.model=model
        self.year=year
c1=Car("Car","Toyota",202,2020)
print("Type of vehicle: ",c1.type,"Brand: ",c1.brand,"Model: ",c1.model,"Year of Manufacturing: ",c1.year)
