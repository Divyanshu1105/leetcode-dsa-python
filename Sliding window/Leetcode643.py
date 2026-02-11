def findMaxAverage(nums ,k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    j = 0
    for i in range(k, len(nums)):
        max_sum += nums[i]
        max_sum -= nums[j]
        j+= 1
        if max_sum > window_sum:
            window_sum = max_sum
    
    return window_sum/k

nums = [1,12,-5]
k = 2
print(findMaxAverage(nums,k))