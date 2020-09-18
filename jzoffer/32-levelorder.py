def levelOrder(root):
    if not root:
        return []
    queue = [root]
    res = []
    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.pop(0)
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return res

def levelOrder(root):
    if not root:
        return []
    queue = [root]
    res = []
    while queue:
        length = len(queue)
        tmp = []
        for i in range(length):
            node = queue.pop(0)
            tmp.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(tmp)
    return res

def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    queue = [root]
    res = []
    cnt = 0
    while queue:
        length = len(queue)
        tmp = []
        for i in range(length):
            node = queue.pop(0)
            tmp.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if cnt%2 == 1:
            tmp = tmp[::-1]
        res.append(tmp)
        cnt += 1
    return res