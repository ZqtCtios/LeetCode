# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        a = []

        def search(root, deep):
            if not root:
                return
            if len(a) == deep:
                a.append(root.val)
            else:
                a[deep] += root.val
            search(root.left, deep+1)
            search(root.right, deep+1)
        search(root, 0)
        max = 0
        maxIndex = 0
        print(a)
        for i in range(len(a)):
            if a[i] > max:
                max = a[i]
                maxIndex = i+1
        return maxIndex
