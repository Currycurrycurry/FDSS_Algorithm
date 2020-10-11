# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast_pointer, slow_pointer = head, head
        while fast_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
            if fast_pointer == slow_pointer:
                new_pointer = head
                while head != fast_pointer:
                    head = head.next
                    fast_pointer = fast_pointer.next
                return head
        return None