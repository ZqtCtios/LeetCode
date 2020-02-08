# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        if root.left is not None:
            self.flatten(root.left)
        if root.right is not None:
            self.flatten(root.right)
        if root.right is None:
            root.right = root.left
            root.left = None
        elif root.left and root.right:
            next = root.left
            while next.right is not None:
                next = next.right
            next.right = root.right
            root.right = root.left
            root.left = None
