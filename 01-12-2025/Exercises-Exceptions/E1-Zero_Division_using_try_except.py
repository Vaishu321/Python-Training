try:
    a=int(input("Enter an integer: "))
    b=int(input("Enter another integer: "))
    Division=a/b
    print("Division:",Division)
except ValueError:
    print("Invalid Number")
except ZeroDivisionError:
    print("Cannot divide by zero")
