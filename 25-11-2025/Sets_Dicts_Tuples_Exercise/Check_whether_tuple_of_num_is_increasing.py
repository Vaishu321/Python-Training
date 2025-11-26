num=(2,3,4,5,6,7)
list0=list(num)
list1=list(num)
new=[]
for i in range (len(list0)):
    y = min(list1)
    new.append(y)
    list1.remove(y)
if new==list0:
    print("Yes its increasing")
else:
    print("No")
