class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
    
        letter = ["a","b","c"]
        counter = 0
        a = ""
        def backtrack(path):

            if len(path) == n:
                nonlocal counter
                counter += 1
                if counter == k:
                    nonlocal a
                    for c in path:
                        a += c
                return

            for i in range(0,3):

                if path and letter[i] == path[-1]:
                    continue
                
                path.append(letter[i])
                backtrack(path)
                path.pop()


        backtrack([])    
       

        return a if a else ""
       