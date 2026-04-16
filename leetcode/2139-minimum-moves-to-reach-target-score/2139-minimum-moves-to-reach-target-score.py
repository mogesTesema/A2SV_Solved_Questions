class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        score = 0
        while maxDoubles > 0 and target > 2:
            remain = target % 2
            target = target //2
            score += remain + 1
            maxDoubles -= 1
        
        score += target - 1
        return score