from typing import List

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        found = False

        def backtrack(start, path):
            nonlocal found

            # early stop if already found
            if found:
                return

            # base case
            if start == len(num):
                if len(path) >= 3:
                    found = True
                return

            for i in range(start, len(num)):
                # avoid leading zeros
                if num[start] == '0' and i > start:
                    break

                curr_str = num[start:i+1]
                curr_num = int(curr_str)

                if len(path) >= 2:
                    if curr_num != path[-1] + path[-2]:
                        continue

                path.append(curr_num)
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return found