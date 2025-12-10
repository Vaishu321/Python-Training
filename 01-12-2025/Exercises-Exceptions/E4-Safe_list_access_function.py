# Build a safe list access function: if index is out of range, return a message instead of error.
def list_access_function(list,item):
    try:
        print(list[item])
    except IndexError:
        print("Index out of range")

list_access_function([1,2,3,4,5],4)
