def move_zeros(nums):
    result=[]
    zero_count=0

    for i in nums:
        if i==0:
            zero_count+=1
        else:
            result.append(i)

    result+=zero_count*[0]
    return result
nums=[0,3,0,5,7,0,9]
print(move_zeros(nums))