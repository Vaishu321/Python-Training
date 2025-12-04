try:
    a=float(input("Enter a number: "))
    b=float(input("Enter another number: "))
    print("Addition(A),Subraction(S),Multiplication(M),Division(D)")
    operation=input("Enter operation: ")
    if operation=="A":
        print('Addition: ',a+b)
    elif operation=="S":
        print('Subtraction: ',a-b)
    elif operation=="M":
        print('Multiplication: ',a*b)
    elif operation=="D":
        print('Division: ',a/b)
    else:
        print("Invalid Operation")
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Cannot divide by zero")
