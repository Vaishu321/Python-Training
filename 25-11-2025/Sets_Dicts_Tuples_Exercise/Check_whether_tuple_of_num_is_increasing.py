num=[2,3,4,5,6,7]
new=[]
for i in num:
    if i+1>1:
        new.append(i)
if new==num:
    print("Yes its increasing")
else:
    print("No")
