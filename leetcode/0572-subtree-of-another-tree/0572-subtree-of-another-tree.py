# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def is_the_same(node_left,node_right):

            if node_left == None and node_right == None:
                return True
            
            if not node_left or not node_right:
                return False

            if node_left.val != node_right.val:
                return False
            
            return is_the_same(node_left.right,node_right.right) and is_the_same(node_left.left,node_right.left)
        
        def subtree(node):

            if node == None:
                return False

            if is_the_same(node,subRoot):
                return True
            
            return subtree(node.left) or subtree(node.right)

        return subtree(root)

            
            