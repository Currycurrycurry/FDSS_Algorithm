# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        tmp = root
        if not root:
            return TreeNode(val)
        while tmp:
            if val < tmp.val:
                if not tmp.left:
                    tmp.left = TreeNode(val)
                    break
                tmp = tmp.left
                continue
            if val > tmp.val:
                if not tmp.right:
                    tmp.right = TreeNode(val)
                    break
                tmp = tmp.right
                continue
        return root
        