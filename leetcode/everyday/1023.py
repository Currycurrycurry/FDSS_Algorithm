# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        array = []
        while head:
            array.append(head.val)
            head = head.next
        return array == list(reversed(array))
    

    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast, prev = head, head, None
        while fast:
            slow = slow.next
            fast = fast.next.next if fast.next else None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        
        return True
    
    # math solution (wrong)
    # 链表节点的值要小于10 + 链表长度还要小于整形最大长度
    def isPalindrome(self, head: ListNode) -> bool:
        s1, s2, t = 0, 0, 1
        while head:
            s1 = s1 * 10 + head.val
            s2 = s2 + t * head.val
            t = t * 10
            head = head.next
        return s1 == s2