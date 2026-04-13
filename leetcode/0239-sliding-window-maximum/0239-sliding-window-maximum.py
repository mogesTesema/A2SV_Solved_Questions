from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # stores indices
        ans = []

        for i in range(len(nums)):
            # Remove indices out of this window
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove smaller elements (they are useless)
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Start adding to result when first window is complete
            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans