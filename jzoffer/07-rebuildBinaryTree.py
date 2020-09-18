class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def rebuildBT(preorder, inorder):
    if not preorder or not inorder or len(preorder) != len(inorder):
        return 
    #    1
    #  2   3
    # 4 5
    # preoder: [1, 2, 4, 5, 3]
    # inorder: [4, 2, 5, 1, 3]
    root_val = preorder[0]
    root_index = inorder.index(root_val)
    root = Node(root_val)
    root.left = rebuildBT(preorder[1:1+root_index], inorder[:root_index])
    root.right = rebuildBT(preorder[1+root_index:], inorder[root_index+1:])
    return root
    

    