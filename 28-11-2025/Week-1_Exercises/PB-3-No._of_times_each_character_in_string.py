str1=input("Enter a string: ")
list1=list(str1.split())
d={}
print(list1)
for i in list1:
    d[i]=list1.count(i)
print(d)
