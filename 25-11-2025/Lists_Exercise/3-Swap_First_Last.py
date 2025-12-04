def swap_first_last(nums):
    nums[0],nums[-1]=nums[-1],nums[0]
    return nums
nums=["a","b","c","d","e"]
print(swap_first_last(nums))
