class Solution:
    def decodeString(self, s: str) -> str:
        
        def dfs(i):
            result = ""
            num = 0
            
            while i < len(s):
                c = s[i]
                
                if c.isdigit():
                    num = num * 10 + int(c)  # handle multi-digit numbers
                
                elif c == '[':
                    decoded,i = dfs(i + 1)
                    result += num * decoded
                    num = 0  # reset after use
                
                elif c == ']':
                    return result, i# end current recursion
                
                else:
                    result += c
                
                i += 1
            
            return result, i
        
        return dfs(0)[0]