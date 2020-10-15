"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root or not root.left:
            return root
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        tmp_root = root
        while tmp_root.left:
            next_root = tmp_root.left
            while tmp_root.next:
                tmp_root.left.next = tmp_root.right
                tmp_root.right.next = tmp_root.next.left
                tmp_root = tmp_root.next
            tmp_root.left.next = tmp_root.right
            tmp_root = next_root
        return root