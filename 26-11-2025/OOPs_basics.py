class Student:
    pass

s1=Student() #new object is being created
s2=Student()

class Student:
    def __init__(self, name, age): #Constructor -- python doesn't take self as a parameter
        self.name = name
        self.age = age


s3=Student("James", 35)
s4=Student("Rahul",14)

print(s3.name, s3.age)

class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print("Brand: ", self.brand)
        print("Model: ", self.model)
        print("Price: ", self.price)

#Creating three car objects
car1= Car("BMW", "Mercedes", 35000000000)
car2= Car("Hyundai","Creta",18000000000)
car3= Car("Toyota","Mercedes",2000000000)

#Displaying details
car1.display()
print()
car2.display()
print()
car3.display()