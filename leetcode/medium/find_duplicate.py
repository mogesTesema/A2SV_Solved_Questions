from collections import Counter
from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        nums_freq = Counter(nums)
        ans = []

        for key,val in nums_freq.items():
            if val == 2:
                ans.append(key)
        return ans
       
        