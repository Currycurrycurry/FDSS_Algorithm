# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def helper(root, path_sum):
            if not root:
                return 0
            path_sum = path_sum * 10 + root.val
            if not root.left and not root.right:
                return path_sum
            return helper(root.left, path_sum) + helper(root.right, path_sum)
        return helper(root,0)