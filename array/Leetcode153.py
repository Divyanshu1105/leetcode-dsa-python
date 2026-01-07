def FindMin(nums):

    # Approach
    # I recognized that the array is originally sorted and 
    # then rotated, which allows the use of binary search instead of linear scanning.

    # I compare the middle element with the rightmost element
    #  to determine which half contains the minimum value.

    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        # Minimum is in the right half
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]

print(FindMin([1,2]))