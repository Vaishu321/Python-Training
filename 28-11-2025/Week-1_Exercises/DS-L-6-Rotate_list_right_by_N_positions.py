list1=[5,6,7,8,9,1,2,3,4]
list2=[]

N=int(input("Enter the number to rotate to right: "))
for i in range(N):
    list2.append(list1[-1])
    list1.remove(list1[-1])
list2.reverse()
list2.extend(list1)
print(list2)
