def find_indices(nums, value):
    result=[]
    for i in range(len(nums)):
        if nums[i]==value:
            result.append(i)
    return result
nums=[5,2,7,5,9,5,3]
value=7
print(find_indices(nums,value))
