class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        letters = ["a", "b", "c"]
        path = []

        def backtrack(k):
            if len(path) == n:
                return "".join(path)

            for ch in letters:
                if path and ch == path[-1]:
                    continue

                remaining = n - len(path) - 1
                count = 2 ** remaining   # size of this subtree

                if k > count:
                    k -= count   # skip this whole branch
                else:
                    path.append(ch)
                    return backtrack(k)

            return ""

        total = 3 * (2 ** (n - 1))
        if k > total:
            return ""

        return backtrack(k)