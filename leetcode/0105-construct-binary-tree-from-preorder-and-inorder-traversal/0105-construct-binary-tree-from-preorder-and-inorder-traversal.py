# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        1.understand the problem
        2. test with edge cases
        duplicate numbers, empty list.
        3. plan solution
          a. get current root node from preorder
          b. get left subtree from inorder elements until root node
          c. get left subtree from inoder, elements from root node to end of inorder.
          repeat untill,all element in subtree used.

        4. impliment plan
            we need:
                root,
                root_index,
                root_index in inorder traversal.

        5. refactor code
        6. done
        """
 
        inorder_map = {val: i for i, val in enumerate(inorder)}
        root_index = 0

        def construct_tree(left, right):
            nonlocal root_index
            if left > right:
                return None

            root_val = preorder[root_index]
            root = TreeNode(root_val)
            root_index += 1

            index = inorder_map[root_val]

            root.left = construct_tree(left, index - 1)
            root.right = construct_tree(index + 1, right)

            return root

        return construct_tree(0, len(preorder) - 1)



        # root_index = 0
        # def construct_tree(left,right):
        #     nonlocal root_index
          
        #     if right - left == 0:
        #         return None
        #     root = TreeNode(preorder[root_index])
        #     index = inorder.index(preorder[root_index])
        #     root_index += 1
        #     root.left = construct_tree(left,index-1)
        #     root.right = construct_tree(index+1,right)

        #     return root

        # return construct_tree(0,len(preorder)-1)


