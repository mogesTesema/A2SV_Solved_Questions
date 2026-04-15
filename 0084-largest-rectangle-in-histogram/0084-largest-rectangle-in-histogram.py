class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            
            poped_index = None
            while stack and stack[-1][0] > h:
                val,index = stack.pop()
                
                
                curr_area = (i-index)* val
                max_area = max(max_area,curr_area)
                poped_index = index

            if poped_index != None:
             stack.append([h,poped_index])
            else:
                stack.append([h,i])
      
        if stack:
            final_h = len(heights)
            for val, index in stack:
                max_area = max(max_area, (final_h - index)*val)

        return max_area