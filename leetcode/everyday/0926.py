# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        paths = []
        path = []
        def helper(root, sum_):
            if not root:
                return
            path.append(root.val)
            sum_ -= root.val
            if not root.left and not root.right and sum_ == 0:
                paths.append(path[:])
            helper(root.left, sum_)
            helper(root.right, sum_)
            path.pop()
        helper(root, sum)
        return paths