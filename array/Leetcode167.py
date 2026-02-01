def twoSum(nums, target):
    l = 0 
    r = len(nums)- 1
    while l < r:
        mid = (l + r)//2
        midVal = nums[mid]
        if nums[l] + nums[r] == target and nums[l] != nums[r]:
            return [l + 1 , r+1]
        elif nums[l] + midVal <= target:
            r-=1
        else:
            l+=1
    return -1


numbers = [0,0,3,4]
target = 0
print(twoSum(numbers,target))