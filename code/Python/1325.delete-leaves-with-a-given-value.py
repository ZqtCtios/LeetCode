# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        self.flag = True
        self.delete(root, target)
        if root.val == target and root.right is None and root.left is None:
            return None
        return root

    def delete(self, root, target, father=None, lr=0):
        if root.left:
            self.delete(root.left, target, root, 0)
        if root.right:
            self.delete(root.right, target, root, 1)
        if root.val == target and root.right is None and root.left is None:
            if father is None:
                root = None
            else:
                if lr == 0:
                    father.left = None
                else:
                    father.right = None
