class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
            ans = defaultdict(int)
            def backtrack(start, path):

                if len(path) >= 2:
                    flag = True
                    for i in range(1, len(path)):
                        if path[i] < path[i - 1]:
                            flag = False
                            break
                    if flag: ans[tuple(path[:])] += 1
                    else: return
                # path.append(nums[start])
                for i in range(start,len(nums)):
                    # if len(path):
                    #     if nums[i] >= nums[i - 1]:
                    #         path.append(nums[i])
                    #         backtrack(i + 1, path)
                    #         path.pop()
                        
                    # else:
                    path.append(nums[i])
                    backtrack(i + 1, path)
                    path.pop()
                
            backtrack(0,[])
            
            return [list(path) for path in ans.keys()]