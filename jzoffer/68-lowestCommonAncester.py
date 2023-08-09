class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def findLowestCommonAncester(root, node1, node2):
    def findTreePath(root, node, path=[]):
        path = path + [root]
        if root == node:
            return path
        if root.left and root.left not in path:
            return findTreePath(root.left, node, path)
        if root.right and root.right not in path:
            return findTreePath(root.right, node, path)
    path1 = findTreePath(root, node1)
    for i in path1:
        print(i.val)
    path2 = findTreePath(root, node2)
    for i in path2:
        print(i.val)
    length = min(len(path1), len(path2))
    for i in range(length):
        if path1[i] == path2[i]:
            continue 
        else:
            return path1[i-1].val
    return path1[length - 1].val


nodes = [Node(i) for i in range(5)]
nodes[0].left = nodes[1]
nodes[0].right = nodes[2]
nodes[1].left = nodes[3]
nodes[2].right = nodes[4]
nodes[3].left = nodes[4]

print(findLowestCommonAncester(nodes[0], nodes[1], nodes[4]))
