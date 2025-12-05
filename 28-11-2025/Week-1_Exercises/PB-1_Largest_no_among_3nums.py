x = float(input("Enter your first number: "))
y = float(input("Enter your second number: "))
z = float(input("Enter your third number: "))

largest = x
if y > largest:
    largest = y
if z > largest:
    largest = z

print("Largest Number:", largest)

#OR

largest1 = max(x,y,z)
print("Largest Number:", largest1)