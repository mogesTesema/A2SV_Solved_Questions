class Solution:
    def numSubarraysWithSum(self, nums, goal):
        def at_most(k):
            if k < 0:
                return 0
            l = 0
            cur = 0
            res = 0
            
            for r in range(len(nums)):
                cur += nums[r]
                
                while cur > k:
                    cur -= nums[l]
                    l += 1
                
                res += r - l + 1
            
            return res
        
        return at_most(goal) - at_most(goal - 1)