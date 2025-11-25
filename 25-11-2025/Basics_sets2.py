#Union
a={1,2,3}
b={3,4,5}
print(a|b)

#Intersection
print(a&b)

#Diff
print(a-b)

#Symmetric Diff
print(a^b)

#Checking if an element is present or not
s={10,20,30}
print(20 in s)  #True

#To iterate through a set
for item in {4,8,12}:
    print(item)

#To remove duplicates in list
nums=[1,2,2,3,3,4]
unique=list(set(nums))

print(unique)