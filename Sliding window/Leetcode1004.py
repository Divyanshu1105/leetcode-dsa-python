def longestOnes(nums, k):
    store = {1: 0, 0: 0}
    maxLen = 0
    j = 0

    for i in range(len(nums)):
        # always include current element first
        store[nums[i]] += 1

        # shrink window if zeros exceed k
        while store[0] > k:
            store[nums[j]] -= 1
            j += 1

        # update length
        currLen = i - j + 1
        if currLen > maxLen:
            maxLen = currLen

    return maxLen


nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(longestOnes(nums, k))
