# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        def printList(node):
            while node:
                print(node.val)
        if not head or not head.next:
            return head
        pre, cur, nex = head, head.next, head.next.next
        v_head = ListNode(0)
        v_head.next = head
        while cur:
            tmp = head
            prev = v_head
            while tmp != cur:
                if tmp.val > cur.val:
                    break
                tmp = tmp.next
                prev = prev.next
            if tmp != cur:
                cur.next = tmp
                pre.next = nex
                prev.next = cur
            pre = tmp
            cur = nex
            if nex:
                nex = nex.next
        return v_head.next

    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummyHead = ListNode(0)
        dummyHead.next = head
        lastSorted = head
        curr = head.next

        while curr:
            if lastSorted.val <= curr.val:
                lastSorted = lastSorted.next
            else:
                prev = dummyHead
                while prev.next.val <= curr.val:
                    prev = prev.next
                lastSorted.next = curr.next
                curr.next = prev.next
                prev.next = curr
            curr = lastSorted.next
        return dummyHead.next

