class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_map = { 
                2: ["a", "b", "c"],
                3: ["d", "e", "f"],
                4: ["g", "h", "i"],
                5: ["j", "k", "l"],
                6: ["m", "n", "o"],
                7: ["p", "q", "r", "s"],
                8: ["t", "u", "v"],
                9: ["w", "x", "y", "z"]
                }

        ans = []
        def backtrack(i,currStr):

            if len(currStr) == len(digits):
                ans.append(currStr)
                return
            
            for c in phone_map[int(digits[i])]:
                backtrack(i+1,currStr + c)
        

        if len(digits) > 0:
            backtrack(0,"")
        return ans
        """
        "23"
        ["ad","ae","af","bd","be","bf","cd","ce","cf"]

        """



    