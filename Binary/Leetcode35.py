def searchInsert(nums,target):
        l = 0
        r = len(nums) -1 
        if nums[0] > target:
            return 0
        while l<=r:
            mid = l + (r - l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target: 
                l = mid + 1
            else:
                r = mid - 1
        return l

nums = [1,3,5,6]
target = 5
print(searchInsert(nums, target))