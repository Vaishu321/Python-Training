n=int(input("Enter the number of positions:"))
new=[]
list=[1,2,3,4,8,9,10,4]
for i in range(n):
    new.append(list[0])
    list.remove(list[0])
list.extend(new)
print(list)

