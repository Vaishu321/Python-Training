def reverse_items_tuple(names):
    reversed_list=[]
    for items in names:
        reversed_list.append(items[::-1])
    print(tuple(reversed_list))

names=["John","May","Henry"]
print((reverse_items_tuple(names)))