class Solution:
    def subarraysWithKDistinct(self, nums, k):
        def at_most(k):
            cnt = {}
            l = 0
            res = 0
            
            for r in range(len(nums)):
                cnt[nums[r]] = cnt.get(nums[r], 0) + 1
                
                while len(cnt) > k:
                    cnt[nums[l]] -= 1
                    if cnt[nums[l]] == 0:
                        del cnt[nums[l]]
                    l += 1
                
                res += r - l + 1
            
            return res
        
        return at_most(k) - at_most(k - 1)