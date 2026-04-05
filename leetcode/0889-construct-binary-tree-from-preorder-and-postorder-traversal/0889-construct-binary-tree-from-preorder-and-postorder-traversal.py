class Solution:
    def constructFromPrePost(self, preorder, postorder):
        post_index = {v: i for i, v in enumerate(postorder)}
        index = 0

        def build(left, right):
            nonlocal index
            if left > right:
                return None

            root = TreeNode(preorder[index])
            index += 1

            if left == right:
                return root

            # next preorder value is left subtree root
            left_root_val = preorder[index]
            mid = post_index[left_root_val]

            root.left = build(left, mid)
            root.right = build(mid + 1, right - 1)

            return root

        return build(0, len(postorder) - 1)