class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def count_from(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.val
            if curr_sum > targetSum:
                return 0
            return (
                (1 if curr_sum == targetSum else 0)
                + count_from(node.left, curr_sum)
                + count_from(node.right, curr_sum)
            )
        
        if not root:
            return 0
        
        return (
            count_from(root, 0)
            + self.pathSum(root.left, targetSum)
            + self.pathSum(root.right, targetSum)
        )