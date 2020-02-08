# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.flag = []
        self.InOrder(root)
        print(self.flag)
        return self.flag[-1]

    def InOrder(self, root, deep=0):
        if root is None:
            return
        if len(self.flag) == deep:
            self.flag.append(root.val)
        self.InOrder(root.left, deep+1)
        self.InOrder(root.right, deep+1)
