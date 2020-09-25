# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return
        root_val = postorder[-1]
        inorder_root_index = inorder.index(root_val)
        root = TreeNode(root_val)
        root.left = self.buildTree(inorder[:inorder_root_index], postorder[:inorder_root_index])
        root.right = self.buildTree(inorder[inorder_root_index+1:], postorder[inorder_root_index:-1])
        return root