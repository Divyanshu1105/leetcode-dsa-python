def sortedSquares(nums):
        i = 0
        j = len(nums)-1
        return_array = [0] * len(nums)
        print(len(return_array))

        for val in range(0,len(nums)):
                nums[val] = nums[val] ** 2
        value = 0
        while i < j :
            if nums[i] < nums[j]:
                j-=1
                i+=1
            else:
                value = nums[i]
                nums[i] = nums[j]
                nums[j] = value
        
        return nums

nums = [-4,-1,0,3,10]
result = sortedSquares(nums)
print(result)