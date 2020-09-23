# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# build a new tree
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        new_value = 0
        if t1:
            new_value += t1.val
        if t2:
            new_value += t2.val
        if t1 or t2:
            root = TreeNode(new_value)
            root.right = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)
            root.left = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
            return root
        return None

    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
        return t1 or t2
    
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        new_value = 0
        if t1:
            new_value += t1.val
        if t2:
            new_value += t2.val
        if t1:
            t1.val = new_value
            t1.left = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
            t1.right = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)
            return t1
        elif t2:
            new_node = TreeNode(new_value)
            new_node.left = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
            new_node.right = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)
            return new_node
        return None
    
