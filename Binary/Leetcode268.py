def missingNumber(nums):
    n = len(nums)
    result = 0
    
    # XOR all indices 0 to n-1 with array elements
    for i in range(n):
        result ^= i ^ nums[i]
    
    # XOR with n (always present in full range 0 to n)
    return result ^ n

num = [3,0,1]
res = missingNumber(num)
print(res)