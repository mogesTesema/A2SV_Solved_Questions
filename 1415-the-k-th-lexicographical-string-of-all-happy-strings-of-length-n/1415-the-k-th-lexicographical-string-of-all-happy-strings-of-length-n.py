class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        unique = []
        letter = ["a","b","c"]
        def backtrack(path):

            if len(path) == n:
                unique.append(path[:])
                return

            for i in range(0,3):

                if path and letter[i] == path[-1]:
                    continue
                
                path.append(letter[i])
                backtrack(path)
                path.pop()


        backtrack([])    
        print(unique)

        if k > len(unique):
            return ""

        ans = ""
        for c in unique[k-1]:
            ans += c
        return ans