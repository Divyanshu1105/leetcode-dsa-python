def containsDuplicate(nums):
        # nums = sorted(nums)
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return False
        # return True  

        seen = {}
        for num in nums:
            if num in seen and seen[num] >= 1:
                return True
            seen[num] = seen.get(num, 0) + 1
        return False

print(containsDuplicate([1,2,3,1]))