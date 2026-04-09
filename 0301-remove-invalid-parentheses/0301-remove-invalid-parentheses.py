from collections import deque

class Solution:
    def removeInvalidParentheses(self, s):
        def isValid(string):
            count = 0
            for c in string:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        res = []
        visited = set()
        queue = deque([s])
        visited.add(s)
        found = False

        while queue:
            curr = queue.popleft()

            if isValid(curr):
                res.append(curr)
                found = True

            if found:
                continue

            for i in range(len(curr)):
                if curr[i] not in ('(', ')'):
                    continue
                nxt = curr[:i] + curr[i+1:]
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)

        return res