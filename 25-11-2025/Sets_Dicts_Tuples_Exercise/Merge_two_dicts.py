
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = {}

# Add items from first dictionary
for key, value in dict1.items():
    merged[key] = value

# Add items from second dictionary
for key, value in dict2.items():
    if key in merged:
        # If key exists, make a list
        if isinstance(merged[key], list):
            merged[key].append(value)
        else:
            merged[key] = [merged[key], value]
    else:
        merged[key] = value

print(merged)  # {'a': 1, 'b': [2, 3], 'c': 4}
