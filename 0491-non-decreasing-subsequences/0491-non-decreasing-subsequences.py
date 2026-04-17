class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
            ans = defaultdict(int)
            def backtrack(start, path):

                if len(path) >= 2:
                    ans[tuple(path[:])] += 1
                # path.append(nums[start])
                for i in range(start,len(nums)):
                    if len(path):
                        if nums[i] >= path[-1]:
                            path.append(nums[i])
                            backtrack(i + 1, path)
                            path.pop()
                        
                    else:
                        path.append(nums[i])
                        backtrack(i + 1, path)
                        path.pop()
                
            backtrack(0,[])
            
            return [list(path) for path in ans.keys()]