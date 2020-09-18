class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        node = head
        while node:
            if node.next and node.next.val == val:
                if node.next.next:
                    tmp = node.next.next
                    node.next = tmp
                else:
                    node.next = None
            node = node.next
        return head