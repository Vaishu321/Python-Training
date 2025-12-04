def string_to_integer(string):
    try:
        return int(string)
    except ValueError:
        print("Invalid String")


Integer = string_to_integer("5")
print(Integer)
