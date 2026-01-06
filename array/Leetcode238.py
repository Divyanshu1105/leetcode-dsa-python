# Implemented an optimized solution using 
# prefix and suffix products to compute the 
# product of array elements except self in O(n) 
# time without using division.

def productExceptSelf(nums):
    n = len(nums)
    ans = [1] * n

    curr = 1
    for i in range(n):
        ans[i] *= curr
        curr *= nums[i]

    curr = 1
    for i in range(n - 1, -1, -1):
        ans[i] *= curr
        curr *= nums[i]

    return ans


nums = [1,2,3,4]
result = productExceptSelf(nums)
print(result)
