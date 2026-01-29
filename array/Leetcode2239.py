def findClosestNumber(nums):
        left = 0
        right = len(nums) - 1
        minVal = 0
        value = float("inf")
        while left < right:
            if nums[left] == nums[right]:
                minVal = nums[left]
            else:
                minVal = min(abs(nums[left]),abs(nums[right]))
            if value > minVal:
                value = minVal
            left += 1
            right -= 1

        if abs(nums[left]) < value:
             return (nums[left])
        return value


nums =[-10000,-10000]
print(findClosestNumber(nums))
