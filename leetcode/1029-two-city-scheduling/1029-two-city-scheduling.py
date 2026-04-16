from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        diffs = []
        
        for city1, city2 in costs:
            
            diffs.append([city1 - city2, city1, city2])
        
        diffs.sort()
        res = 0

        for i in range(len(diffs)):
            if i < len(diffs) // 2:
                res += diffs[i][1]  
            else:
                res += diffs[i][2] 
                
        return res