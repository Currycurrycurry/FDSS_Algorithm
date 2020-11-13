class Solution:
    # why logic so complicated
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        node = head
        second_head = head.next
        while node and node.next:
            next_node = node.next
            node.next = node.next.next
            node = next_node

        final_node = head
        while final_node.next:
            final_node = final_node.next
        final_node.next = second_head
        return head

    # the logic is so clear...
    def addEvenList(self, head):
        if not head or head.next:
            return head
        point1, point2 = head, head.next
        p1, p2 = point1, point2
        while p2 and p2.next:
            p1.next = p1.next.next
            p2.next = p2.next.next
            p1 = p1.next
            p2 = p2.next
        p1.next = point2
        return point1
        
