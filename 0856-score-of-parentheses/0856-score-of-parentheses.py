class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        stack = []


        for c in s:
            if c == "(":
                stack.append(c)
            else:
                curr_score = 0

                while stack[-1] != "(":
                    curr_score += stack.pop()
                if curr_score != 0:
                    curr_score *=2
                else:
                    curr_score = 1
                stack.pop()
                stack.append(curr_score)
        return sum(stack)
    