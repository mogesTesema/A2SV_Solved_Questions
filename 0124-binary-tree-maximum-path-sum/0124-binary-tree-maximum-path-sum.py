# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        ans = float("-inf")

        def traverse(node):
            nonlocal ans

            if node == None:
                return 0
            
            val = node.val
            left_val = max(traverse(node.left),0)
            right_val = max(traverse(node.right),0)

            curr_val =left_val + right_val + val
            ans = max(ans,curr_val)
            

            return max(left_val,right_val) + val
        a = traverse(root)
        return max(ans,a)

        