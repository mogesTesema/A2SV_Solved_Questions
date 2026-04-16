import math

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        curr = nums[-1]
        operations = 0

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= curr:
                curr = nums[i]
            else:
                k = math.ceil(nums[i] / curr)
                operations += k - 1
                curr = nums[i] // k

        return operations