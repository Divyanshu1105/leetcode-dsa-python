def subsets(nums):
    """
    Generate all possible subsets of a given array using decision tree backtracking.
    
    Implements the classic "Include/Exclude" decision tree approach for power set generation. 
    Time: O(n * 2^n), Space: O(n) recursion stack
    Generates exactly 2^n subsets using systematic decision tree exploration.
    """
    result = []
    def solve(index, path):
        if len(nums) == index:
            result.append(path)
            return 

        solve(index + 1 , path + [nums[index]]) #inclusive call
        solve(index + 1, path) #exclusive call 
    solve(0,[])
    return result

nums = [1,2,3]
res = subsets(nums)
print(res)