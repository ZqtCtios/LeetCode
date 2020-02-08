# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        l = self.getList(root)
        return l[k-1]

    def getList(self, root):
        l = [root.val]
        if root.left:
            l = self.getList(root.left)+l
        if root.right:
            l = l+self.getList(root.right)
        return l
