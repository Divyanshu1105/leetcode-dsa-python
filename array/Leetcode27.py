class Solution:
    def removeElement(self,nums, value):
        count = 0
        k = 0
        remain = 1
        for i in range(0,len(nums)):
            if nums[i] == value:
                count+=1
        


if __name__ == "__main__":
    obj = Solution()
    target = 2
    nums = [0,0,1,1,2,2,3,3,4]
    result = obj.removeElement(nums,target)