class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        unique = []
        letter = ["a","b","c"]
        def backtrack(start ,path):

            if len(path) == n:
                unique.append(path[:])
                return

            for i in range(0,3):

                if path and letter[i] == path[-1]:
                    continue
                
                path.append(letter[i])
                backtrack(i+1,path)
                path.pop()


        backtrack(0,[])    
        print(unique)

        if k > len(unique):
            return ""

        ans = ""
        for c in unique[k-1]:
            ans += c
        return ans