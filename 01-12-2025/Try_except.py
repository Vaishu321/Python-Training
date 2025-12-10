try:
    num=int(input("Enter a number: "))
    print(10/num)
except ValueError:
    print("Invalid Number")
except ZeroDivisionError:
    print("Cannot divide by zero")