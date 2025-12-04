class Customer:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    def loyalty_program(self):
        if self.age > 25:
            return "You are eligible for loyalty program"
        else:
            return "You are not eligible for loyalty program"
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("City:", self.city)
        print("Loyalty program:", self.loyalty_program())

C1=Customer("James", 25, "California")
C2=Customer("Bob", 27, "Delhi")
C1.display()
C2.display()
