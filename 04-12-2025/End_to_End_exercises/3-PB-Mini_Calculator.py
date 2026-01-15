def mini_calculator(a,b,function):
    if function=="add":
        return a+b
    elif function=="subtract":
        return a-b
    elif function=="multiply":
        return a*b
    elif function=="divide":
        return a/b
    else:
        return "Invalid Input"


a=int(input("Enter your first number: "))
b=int(input("Enter your second number: "))
print(mini_calculator(a,b,input("Enter the function: ")))