tuple1=(1,2,5,42,57,35)
list1=list(tuple1)

largest=max(list1)
list1.remove(largest)
second_largest=max(list1)
print(second_largest)