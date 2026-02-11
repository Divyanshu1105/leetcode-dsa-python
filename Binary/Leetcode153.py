def findMin(nums):
    """
        Find the minimum element in a rotated sorted array.
        
        Uses binary search to find the pivot point (smallest element)
        in O(log n) time.
    """
    l = 0
    r = len(nums) - 1
    while l < r:
        mid = (l + r)//2
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid
    
    return nums[l]


nums = [1,2,3,4]
print(findMin(nums))