class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.parent = None
        self.val = val
    
# 中序遍历的下一个节点
def findNextNode_inorder(root):
    next_node = root
    if root.right:
        tmp = root.right
        next_node = tmp
        while tmp.left:
            next_node = tmp.left
            tmp = tmp.left
    else:
        if root.parent:
            if root.parent.left == root:
                next_node = root.parent
            elif root.parent.parent:
                next_node = root.parent.parent
    return next_node

# 前序遍历的下一个节点
def findNextNode_preorder(root):
    pass




