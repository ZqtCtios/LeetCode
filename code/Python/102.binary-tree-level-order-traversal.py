# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []

        def search(root, deep):
            if not root:
                return
            if len(res) == deep:
                res.append([root.val])
            else:
                res[deep].append(root.val)
            search(root.left, deep+1)
            search(root.right, deep+1)
        search(root, 0)
        return res
