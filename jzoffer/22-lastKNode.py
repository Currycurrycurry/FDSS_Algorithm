class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        max_step = k
        fast_node = head
        for _ in range(max_step):
            fast_node = fast_node.next
        while fast_node:
            head = head.next
            fast_node = fast_node.next
        return head
