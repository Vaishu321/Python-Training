#Create a class Product with attributes name, price, quantity. Add a method to calculate the total cost of all quantities.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity
    def display(self):
        print("Product: ",self.name)
        print("Price: ",self.price)
        print("Quantity: ",self.quantity)
        print("Total Price: ",self.total_price())

P1=Product("Jam","100",1)
P2=Product("Biscuit","50",2)
P1.display()
