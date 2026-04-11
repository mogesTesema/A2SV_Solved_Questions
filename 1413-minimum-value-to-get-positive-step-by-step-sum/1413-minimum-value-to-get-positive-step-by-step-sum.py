class Solution:
    def minStartValue(self, nums):
        cur = 0
        mn = 0
        
        for x in nums:
            cur += x
            mn = min(mn, cur)
        
        return 1 - mn