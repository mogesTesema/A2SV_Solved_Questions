class Solution:
    def checkSubarraySum(self, nums, k):
        mp = {0: -1}
        cur = 0
        
        for i, x in enumerate(nums):
            cur += x
            if k != 0:
                cur %= k
            
            if cur in mp:
                if i - mp[cur] > 1:
                    return True
            else:
                mp[cur] = i
        
        return False