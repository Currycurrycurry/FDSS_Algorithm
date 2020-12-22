import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        heap = collections.deque([root])
        res = []
        i = 0
        while len(heap) > 0:
            tmp = []
            for _ in range(len(heap)):
                node = heap.popleft()
                tmp.append(node.val)
                if node.left:
                    heap.append(node.left)
                if node.right:
                    heap.append(node.right)
            if i % 2 == 1:
                tmp = tmp[::-1]
            res.append(tmp)
            i += 1
        return res