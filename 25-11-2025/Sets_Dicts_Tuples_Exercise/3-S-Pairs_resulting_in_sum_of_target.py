def find_pairs(nums, target):
    pairs = []
    nums = list(nums)  # Convert set to list
    for i in range(len(nums)):
        for j in range(i, len(nums)):  # Start from i to avoid repeating pairs
            if nums[i] + nums[j] == target:
                pairs.append((nums[i], nums[j]))
    return pairs

nums={2,4,6,8,10}
target=8
print(find_pairs(nums, target))
