class Solution:
    def shiftingLetters(self, s, shifts):
        n = len(s)
        diff = [0] * (n + 1)
        
        for l, r, d in shifts:
            val = 1 if d == 1 else -1
            diff[l] += val
            diff[r + 1] -= val
        
        cur = 0
        res = []
        
        for i in range(n):
            cur += diff[i]
            shift = cur % 26
            ch = (ord(s[i]) - ord('a') + shift) % 26
            res.append(chr(ch + ord('a')))
        
        return "".join(res)