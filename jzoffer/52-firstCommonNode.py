# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def getLen(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        len_a = getLen(headA)
        len_b = getLen(headB)
        tmp_a = headA
        tmp_b = headB
        if len_b > len_a:
            diff = len_b - len_a
            while diff > 0:
                tmp_b = tmp_b.next
                diff -= 1
        else:
            diff =  len_a - len_b
            while diff > 0:
                tmp_a = tmp_a.next
                diff -= 1
        while tmp_a and tmp_b and tmp_a != tmp_b:
            tmp_a = tmp_a.next
            tmp_b = tmp_b.next
        return tmp_a