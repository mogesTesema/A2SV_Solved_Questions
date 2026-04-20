# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def build(left,right):
            if left == right:
                return  TreeNode(nums[left])
            if left > right:
                return
            
            curr_max = max(nums[left:right+1])
            index_max = nums.index(curr_max)
            node = TreeNode(curr_max)
            node.left = build(left,index_max-1)
            node.right = build(index_max+1, right)

            return node

        return build(0,len(nums)-1)