from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        word_set = set(wordDict)   # faster lookup
        sentences = []

        def get_words(start, path):
            # base case
            if start == len(s):
                sentences.append(" ".join(path))
                return
            
            word = []
            for i in range(start, len(s)):
                word.append(s[i])
                word_string = "".join(word)

                # only proceed if valid word
                if word_string in word_set:
                    path.append(word_string)
                    get_words(i + 1, path)
                    path.pop()   # backtrack

        get_words(0, [])
        return sentences