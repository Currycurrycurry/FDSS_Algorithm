# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 一个贼nb的写法
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)
        pre, cur = tee(inorder(root))
        next(cur, None)
        return min(b-a for a, b in zip(pre, cur))

class Solution:
    def __init__(self):
        self.res = float('inf')
        self.preVal = -1

    def getMinimumDifference(self, root: TreeNode) -> int:
        def inorder(root):
            if not root:
                return
            inorder(root.left)

            if self.preVal < 0:
                self.preVal = root.val
            else:
                tmp = root.val - self.preVal
                self.res = min(tmp, self.res)
                self.preVal = root.val
                
            inorder(root.right)
        inorder(root)
        return self.res
