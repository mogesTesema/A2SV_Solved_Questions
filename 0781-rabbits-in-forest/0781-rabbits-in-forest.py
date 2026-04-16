from typing import List
from collections import Counter
import math

class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        rabbits = Counter(answers)
        total = 0

        for rabbit, freq in rabbits.items():
            group_size = rabbit + 1
            groups = math.ceil(freq / group_size)
            total += groups * group_size

        return total