def bubSort(nums):
    for i in range(len(nums)-1):
        j = i+1
        while j < len(nums):
            if nums[i] > nums[j]:
                #swap try to swap using ^
                nums[i] = nums[i] ^ nums[j]
                nums[j] = nums[i] ^ nums[j]
                nums[i] = nums[i] ^ nums[j]
            j+=1
    return nums


nums = [5,2,7,1,8,3,2,1]
print(bubSort(nums))
