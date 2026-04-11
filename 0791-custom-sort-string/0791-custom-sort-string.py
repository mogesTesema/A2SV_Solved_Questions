class Solution:
    def customSortString(self, order: str, s: str) -> str:

        freq = Counter(s)

        ans = ""

        for char in order:
            if char in freq:
                ans += char*freq[char]
                freq[char] = 0
        for key, val in freq.items():
            if val > 0:
                ans += key*val
        
        
        return ans
        