#Calculate the max and min of tuples without using max and min
numbers=(33,20,30,60,50)

def max_min(nums):
    min_value = nums[0]
    max_value = nums[0]

    for i in range(1,len(nums)):
        if nums[i] > max_value:
            max_value = nums[i]
        elif nums[i] < min_value:
            min_value = nums[i]
    return max_value,min_value
print(max_min(numbers))
