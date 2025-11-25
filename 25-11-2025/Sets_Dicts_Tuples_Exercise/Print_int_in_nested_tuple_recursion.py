def print_integers(data):
    for item in data:
        if isinstance(item, int):  # If item is an integer
            print(item)
        elif isinstance(item, tuple):  # If item is a tuple, recurse
            print_integers(item)
nested_tuple = (10, (20, 30), (40, (50, 60)))
print_integers(nested_tuple)
