# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        virtual_head = ListNode(0)
        virtual_head.next = head
        tmp_node = virtual_head
        while tmp_node:
            next_node = tmp_node.next
            if next_node:
                next_next_node = next_node.next
            else:
                next_next_node = None
            if next_node and next_next_node:
                tmp_node.next = next_next_node
                next_node.next = next_next_node.next
                next_next_node.next = next_node
                tmp_node = next_node
            else:
                break
        return virtual_head.next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        next = head.next
        head.next = self.swapPairs(next.next)
        next.next = head
        return next