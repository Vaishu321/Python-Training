class Calculator:
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2
    def add(self):
        answer=self.number1+self.number2
        print("Addition is ",answer)
    def subtract(self):
        answer=self.number1-self.number2
        print("Subtraction is", answer)
    def multiply(self):
        answer=self.number1*self.number2
        print("Multiplication is",answer)
    def divide(self):
        if self.number2==0:
            print("Division by 0 is not possible")
        else:
            answer=self.number1/self.number2
            print("Division is ",answer)
    def display(self):
            print("Number 1=", self.number1)
            print("Number 2=", self.number2)

a=Calculator(int(input("Enter number1: ")),int(input("Enter number2: ")))

operation=(input("Enter operation: "))
a.display()
if operation=="Add":
    a.add()
elif operation=="Subtract":
    a.subtract()
elif operation=="Multiply":
    a.multiply()
elif operation=="Divide":
    a.divide()
else:
    print("Invalid operation")

