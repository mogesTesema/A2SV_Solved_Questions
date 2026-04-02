from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # Iterate through every possible hour (0-11) and minute (0-59)
        return [
            f"{h}:{m:02d}" 
            for h in range(12) for m in range(60)
            if (bin(h) + bin(m)).count('1') == turnedOn
        ]
