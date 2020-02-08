# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.flag = []
        self.Search(root)
        print(self.flag)
        return self.flag[-1]

    def Search(self, root, deep=0):
        if root is None:
            return
        if len(self.flag) == deep:
            self.flag.append(root.val)
        self.Search(root.left, deep+1)
        self.Search(root.right, deep+1)
