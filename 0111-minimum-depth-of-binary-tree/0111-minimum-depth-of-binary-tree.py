# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        min_depth = float('inf')

        def dsf(node,depth):
            depth += 1
            if not node:
                return

            if node.left == None and node.right == None:
                nonlocal min_depth
                min_depth = min(min_depth,depth)

            
            dsf(node.left,depth)
            dsf(node.right,depth)

        dsf(root,0)
        return 0 if min_depth == float('inf') else min_depth

        