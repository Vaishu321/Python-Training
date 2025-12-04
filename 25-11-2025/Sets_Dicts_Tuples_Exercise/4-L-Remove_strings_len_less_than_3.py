new = []
def less_than_3(list):
    for item in list:
        if len(item)>3:
            new.append(item)
    print(new)

list=["Mary","Sue","john","Hello"]
print(less_than_3(list))
