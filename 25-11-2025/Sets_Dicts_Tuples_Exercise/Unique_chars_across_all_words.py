def unique_chars(list):
    chars = set()
    for item in list:
        chars.update(item)
    print(chars)

list=["Hello","World"]
unique_chars(list)