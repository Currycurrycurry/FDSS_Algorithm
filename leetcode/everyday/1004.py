# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        virtual_head = ListNode(0)
        tmp = virtual_head
        carry = 0
        while l1 and l2:
            val = (l1.val + l2.val + carry) % 10 
            carry = (l1.val + l2.val + carry) // 10
            tmp.next = ListNode(val)
            tmp = tmp.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            tmp.next = ListNode((l1.val + carry) % 10)
            carry = (l1.val + carry) // 10
            tmp = tmp.next
            l1 = l1.next
        while l2:
            tmp.next = ListNode((l2.val + carry) % 10)
            carry = (l2.val + carry) // 10
            tmp = tmp.next
            l2 = l2.next
        if carry:
            tmp.next = ListNode(carry)
        return virtual_head.next