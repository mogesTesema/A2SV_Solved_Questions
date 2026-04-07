# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.moves = 0
        
        def dfs(node):
            if not node:
                return 0
            
            left_balance = dfs(node.left)
            right_balance = dfs(node.right)
            
            # Count moves needed for left and right subtrees
            self.moves += abs(left_balance) + abs(right_balance)
            
            # Return net balance to parent
            return node.val + left_balance + right_balance - 1
        
        dfs(root)
        return self.moves