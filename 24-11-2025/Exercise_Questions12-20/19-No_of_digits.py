num=int(input("Enter a number: "))


count = 0
n = abs(num)
while n > 0:
    n //= 10
    count += 1
print(count) 
