def find_duplicates(arr):
    duplicates = []
    seen = set()
    for item in arr:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        else:
            seen.add(item)
    return duplicates
array=[1,2,3,2,4,1,5,1]
print(sorted(find_duplicates(array)))