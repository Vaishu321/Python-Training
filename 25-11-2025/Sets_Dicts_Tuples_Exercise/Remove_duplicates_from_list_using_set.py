def remove_duplicates(nums):
    set1=set(nums)
    return list(set1)

nums=[1,2,3,5,4,6,5,6,7,8,9]
print(remove_duplicates(nums))