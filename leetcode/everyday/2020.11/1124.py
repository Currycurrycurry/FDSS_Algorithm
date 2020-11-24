# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        cnt = 0
        def pre_order(root):
            if root:
                nonlocal cnt
                cnt += 1
                pre_order(root.left)
                pre_order(root.right)
        pre_order(root)
        return cnt
    

    def countNodes(self, root: TreeNode) -> int:
        def getHeight(node):
            height = 0
            while node:
                node = node.left
                height += 1
            return height
        if root:
            left_height, right_height = getHeight(root.left), getHeight(root.right)
            if left_height == right_height:
                return (1 << left_height) + self.countNodes(root.right)
            else:
                return (1 << right_height) + self.countNodes(root.left)
        else:
            return 0
            