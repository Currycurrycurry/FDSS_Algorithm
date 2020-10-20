# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# wrong code
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
                return
        def helper(first_node, last_last_node=None):
            if not last_last_node:
                last_last_node = head
                while last_last_node.next and last_last_node.next.next:
                    last_last_node = last_last_node.next
            last_node = last_last_node.next
            if first_node == last_node:
                return
            if first_node.next == last_node:
                return
            first_node.next = last_node
            last_node.next = first_node.next
            helper(first_node.next, last_last_node)
        helper(head)