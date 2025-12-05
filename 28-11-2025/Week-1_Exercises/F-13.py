
def average(nums):
    if not nums:
        raise ValueError("Cannot compute average of an empty list")
    return sum(nums) / len(nums)

print(average([10, 20, 30]))  # 20.0
