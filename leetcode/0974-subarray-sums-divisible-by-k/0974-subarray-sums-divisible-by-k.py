class Solution:
    def subarraysDivByK(self, nums, k):
        freq = {0: 1}
        cur = 0
        ans = 0
        
        for x in nums:
            cur += x
            mod = cur % k
            
            if mod < 0:
                mod += k
            
            ans += freq.get(mod, 0)
            freq[mod] = freq.get(mod, 0) + 1
        
        return ans