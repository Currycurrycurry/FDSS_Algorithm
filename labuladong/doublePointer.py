class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# 1. 快慢指针-链表
# 判断链表中是否含有环
def hasCircle(node):
    fast = node
    slow = node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False

# 已知链表中含有环 返回环的起始位置
# 关键： 当快慢指针相遇时，让其中任何一个指针指向头节点，然后以相同速度前进，再次相遇时所在的节点位置就是环开始的位置。
def detectCircle(node):
    slow = node
    fast = node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    slow = node
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow

# 寻找链表的中点
def findMiddle(node):
    slow, fast = node, node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

# 寻找链表的倒数第k个元素
def findLastKthNode(node, k):
    slow, fast = node, node
    while k >= 1:
        k -= 1
        fast = fast.next
    
    while fast:
        slow = slow.next
        fast = fast.next
    
    return slow


# 2. 左右指针-数组/字符串
# TODO 两数之和
# TODO 反转数组

