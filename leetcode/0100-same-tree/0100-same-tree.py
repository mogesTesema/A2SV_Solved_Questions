# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:


        def same_tree(left_node,right_node):

            if left_node == None and right_node != None or left_node != None and right_node == None:
                return False
            if left_node == None and right_node == None:
                return True

            if left_node.val != right_node.val:
                return False

            return same_tree(left_node.left, right_node.left) and same_tree(left_node.right,right_node.right)
        
        return same_tree(p,q)

        # def is_same(p,q):

        #     if ((q is None) ^ (p is None)):
        #         return False
        #     if q==None and p==None:
        #         return True
            
        #     if q.val != p.val:
        #         return False
        #     return is_same(q.left,p.left) and is_same(q.right,p.right)

        # is_same(q,p)
            
        