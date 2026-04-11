class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        candidate =[x for x in range(int(sqrt(c))+1)] 
        left = 0
        right = len(candidate) - 1 
        print(candidate)
        # if isqrt(c):
        #     return True

        while left <= right:
            curr = candidate[left]**2 + candidate[right]**2

            if curr == c:
                return True
            if curr > c:
                right -= 1
            else:
                left += 1
        return False
