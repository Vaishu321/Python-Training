mixed=("hello",9,2,"Why","Sorry")
strings=[]
nums=[]

list=list(mixed)
for items in list:
    if type(items)==str:
        strings.append(items)
    else:
        nums.append(items)

print(tuple(strings))
print(tuple(nums))
