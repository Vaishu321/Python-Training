largest =0
second=0
array=[27,94,329,2039,10]
for i in array:
    if i>largest:
        second = largest
        largest=i

    elif (i<largest) and (i>second):
        second=i

print(largest)
print(second)