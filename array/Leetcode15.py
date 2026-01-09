def threeSum(nums):
    #first sort the array and used two pointer approach
    """
    Sort + Two Pointers approach to find all unique triplets summing to zero.

    Time Complexity: O(n²) - Single sort O(n log n) + O(n) per i-loop (two pointers)
    Space Complexity: O(1) extra space (excluding output array)
    """

    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicates for i
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result

res = threeSum([-1,0,1,2,-1,-4])
print(res)