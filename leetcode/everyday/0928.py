"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# 树的层序遍历 非常睿智一题
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return 
        heap = deque([root])
        while heap:
            size = len(heap)
            for i in range(size):
                node = heap.popleft()
                if i + 1 < size:
                    node.next = heap[0]
                if node.left:
                    heap.append(node.left)
                if node.right:
                    heap.append(node.right)
        return root