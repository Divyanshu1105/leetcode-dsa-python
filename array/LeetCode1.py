# class Solution:
#     def twoSum(self, nums, target):
#         for i in range(0, len(nums)-1):
#             for j in range(i+1, len(nums)):  # Corrected: range starting from i+1
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

# list1 = [1, 2, 4, 7]
# target = 9

# obj = Solution()
# result = obj.twoSum(list1, target)
# print(result)  # Outputs: [1, 3] since 2 + 7 = 9

class Solution:
    def testing(self,arr):
        arr = sorted(arr)
        return arr
        

if __name__ == '__main__':
    obj = Solution()
    arr = [2,6,1,8,4,3]
    result = obj.testing(arr)
    print(result)
