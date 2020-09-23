# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def getTreeSum(root):
            return getTreeSum(root.left) + root.val + getTreeSum(root.right) if root else 0
        sum_value = getTreeSum(root)
        def helper(root):
            if root:
                helper(root.left)
                nonlocal sum_value
                sum_value -= root.val
                root.val = sum_value + root.val
                helper(root.right)
        helper(root)
        return root