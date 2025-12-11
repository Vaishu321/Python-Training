#Since it must be ordered we cant use set
product_list=[13,45,67,78,34,78,34]
new=[]
for i in product_list:
    if i not in new:
        new.append(i)

print(new)
