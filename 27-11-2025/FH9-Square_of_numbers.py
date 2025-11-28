#Write a program that writes the squares of numbers from 1 to 10 into a file ( numbers.txt ), one per
#line.

with open("numbers.txt","w") as file:
    for i in range(1,11):
        square=i**2
        file.write(str(square)+"\n")

