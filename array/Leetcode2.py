def sorting(nums):
    k = 0
    j = 1
    for i in range(0,len(nums)-1):
        while j < len(nums):
            if nums[i] == nums[j]:
                j+=1
                continue
            else:
                if k+1 == len(nums):
                    break
                nums[k+1] = nums[j]
                k+=1
                j+=1
                break

    return nums[0:k+1]

nums = [0,1,1,1,2,2,2,3,3,3,3,4,5]
result = sorting(nums)
print(result)