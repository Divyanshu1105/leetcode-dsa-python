def summaryRanges(nums):
    if not nums:
            return []
    
    if len(nums) == 1:
        return nums[0]
    
    i = 0
    result = []
    while i < len(nums):
        j = i
        while j < len(nums):
            if j < len(nums) - 1 and nums[j] + 1 == nums[j+1]:
                j+=1
            else:
                if i == j:
                    result.append(f"{nums[i]}")
                else:
                    result.append(f"{nums[i]}->{nums[j]}")
                break
        i = j + 1
    return result


nums = [0,2,3,4,6,8,9]

res = summaryRanges(nums)
print(res)