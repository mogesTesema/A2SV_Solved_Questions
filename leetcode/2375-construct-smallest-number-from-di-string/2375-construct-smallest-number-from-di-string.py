class Solution:
    def smallestNumber(self, pattern: str):

        nums = [str(i) for i in range(1, 10)]
        ans = None

        def backtrack(path):
            nonlocal ans

            if len(path) == len(pattern) + 1:
                ans = "".join(path)
                return True

            for num in nums:
                if num in path:
                    continue

                i = len(path)

                if i > 0:
                    if pattern[i - 1] == 'I' and path[-1] >= num:
                        continue
                    if pattern[i - 1] == 'D' and path[-1] <= num:
                        continue

                path.append(num)
                if backtrack(path):
                    return True
                path.pop()

            return False

        backtrack([])
        return ans