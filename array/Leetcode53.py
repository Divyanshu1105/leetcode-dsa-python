def maxSubarr(nums):
    currSum = nums[0]
    maxSum = nums[0]

    for i in range(1, len(nums)):
        currSum = max(nums[i], currSum + nums[i])
        maxSum = max(maxSum, currSum)
    return maxSum

nums = [-2,1,-3,4,-1,2,1,-5,4]
result = maxSubarr(nums)
print(result)