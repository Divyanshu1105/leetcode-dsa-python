def plusOne(nums):
    i = len(nums)-1
    nums[i] = nums[i] + 1
    carry = 0
    while i >= 0:
        sum = nums[i] + carry
        if sum == 10:
            carry = 1
            nums[i] = 0
            sum = 0
        else:
            nums[i] = nums[i] + carry
            carry = 0
            sum = 0
        i -=1
    if carry == 1:
        nums.append(0) 
        for i in range(len(nums)-1, -1, -1):
            nums[i] = nums[i - 1]
            if i == 0:
                nums[0] = 1    
    return nums

nums = [9,9,9,9]
result = plusOne(nums)
print(result)