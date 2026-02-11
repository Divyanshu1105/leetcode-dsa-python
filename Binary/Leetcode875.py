class Solution:
    def eating(self , k, piles):
        ceiled = 0
        for pile in piles:
            ceiled += -(-pile//k)
        return ceiled

    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles)
    
        while l < r:
            mid = (l + r) // 2
            hours_needed = self.eating(mid, piles)
            
            if hours_needed <= h:
                r = mid 
            else:
                l = mid + 1
        
        return l
        
obj = Solution()
piles = [30,11,23,4,20]
h = 5

res = obj.minEatingSpeed(piles,h)
print(res)