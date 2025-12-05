str1=input("Enter a string: ")
list1=list(str1)
d={}
for i in list1:
    if i=="!" or i=="@" or i=="#" or i=="$" or i=="%" or i=="^" or i=="&" or i=="*" :
        str1=str1.replace(i,"")

print(str1)