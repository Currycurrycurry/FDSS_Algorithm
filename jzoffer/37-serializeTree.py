class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'
        res = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                res.append(str(node.val))
            else:
                res.append('null')
        print(res)
        return '[' + ','.join(res) + ']'
    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '[]': return None
        res = data[1:-1].split(',')
        for i,r in enumerate(res):
            if r == 'null':
                res[i] = None
            else:
                res[i] = int(res[i])

        if len(res) == 0:
            return None
        index = 1
        root = TreeNode(res[0])
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if res[index] != None:
                node.left = TreeNode(res[index])
                queue.append(node.left)
            index += 1
            if res[index] != None:
                node.right = TreeNode(res[index])
                queue.append(node.right)
            index += 1
        return root
