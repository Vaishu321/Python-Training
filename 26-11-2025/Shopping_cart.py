class ShoppingCart:
    def __init__(self):
        self.items=[] #Each value will be a tuple
    def add_item(self,name,price):
        self.items.append((name,price))
        print(name,"Added to cart")
    def remove_item(self,name):
        for item in self.items:
            if item[0]==name:
                self.items.remove(item)
                print(name,"Removed from cart")
                return
            print(name,"Item not in cart")

    def total_cost(self):
        total=0
        for item in self.items:
            total+=item[1]
        return total

    def discount_items(self,percent):
        total=self.total_cost()
        discount=(total*percent/100)
        final_price=total-discount
        print("Discounted price:",final_price)
        return final_price
    def display_items(self):
        if not self.items:
            print("Cart is Empty")
        else:
            print("Items in cart:")
            for name,price in self.items:
                print(name,":",price)

#Testing the class
cart=ShoppingCart()
cart.add_item("Milk",100)
cart.add_item("Chocolate",200)
cart.add_item("Pillow",300)
cart.add_item("Phone case",400)
cart.remove_item("Milk")
cart.display_items()
print("Total Cost:",cart.total_cost())
cart.discount_items(10)


