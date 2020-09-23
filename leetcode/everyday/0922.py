# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 哎 我是不是一辈子也写不出来这么nb的代码
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(root):
            l = 2
            r = 2
            if root.left:
                l = dfs(root.left)
            if root.right:
                r = dfs(root.right)
            if l == 0 or r == 0:
                nonlocal total
                total += 1
                return 1
            elif l == 1 or r == 1:
                return 2
            return 0
        total = 0
        if not root:
            return total
        if dfs(root) == 0:
            total += 1
        return total