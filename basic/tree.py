class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class ThreeNode(Node):
    def __init__(self, val):
        Node.__init__(self, val)
        self.mid = None
    
def build3aryTree(arr):
    pass

def preorder(root):
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []

def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []

def postorder(root):
    return postorder(root.left) + postorder(root.right) + [root.val] if root else []

def levelorder(root):
    res = []
    heap = []
    heap.append(root)
    while len(heap) > 0:
        node = heap.pop(0)
        if node.left:
            heap.append(node.left)
        if node.right:
            heap.append(node.right)
        res.append(node.val)
    return res

def isSameTree(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    return root1.val == root2.val and isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)

def isSimilarTree(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    return isSimilarTree(root1.left, root2.left) and isSimilarTree(root1.right, root2.right)

def ifExistNode(root, node):
    if not root:
        return False
    if root == node:
        return True
    return ifExistNode(root.left, node) or ifExistNode(root.right, node)

def hasSubTree(big_tree_root, small_tree_root):
    if tree1 and tree2:
        if tree1.val == tree2.val:
            return sub_tree(tree1.left, tree2.left) and sub_tree(tree1.right, tree2.right)
        else:
            return sub_tree(tree1.left, tree2) or sub_tree(tree1.right, tree2)
    if not tree1 and tree2:
        return False
    return True


nodes = [Node(i) for i in range(10)]
root = nodes[5]
root.left = nodes[3]
root.right = nodes[6]
nodes[3].left = nodes[1]
nodes[3].right = nodes[4]
nodes[6].right = nodes[7]

print(preorder(root))
print(inorder(root))
print(postorder(root))
print(levelorder(root))




