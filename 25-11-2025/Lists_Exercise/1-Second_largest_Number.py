nums=[23,89,12,78,55,42]

def second_largest(nums):
    largest =nums[0]
    second=nums[0]

    for n in nums:
        if n > largest :
            largest =n

    for n in nums:
        if n != largest and n>second:
            second=n

    return second

print(second_largest(nums))
