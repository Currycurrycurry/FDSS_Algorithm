# 递归操作链表并不高效。
# 和迭代解法相比，虽然时间复杂度都是 O(N)，但是迭代解法的空间复杂度是 O(1)，而递归解法需要堆栈，空间复杂度是 O(N)。
# 所以递归操作链表可以作为对递归算法的练习或者拿去和小伙伴装逼，但是考虑效率的话还是使用迭代算法更好。
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class HeapNode():
    def __init__(self, node: Node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

# 21.合并两个有序列表
# 拉拉链/蛋白酶合成蛋白质 
# 虚拟头节点技巧
def mergeTwoLists(list1, list2):
    # 虚拟头节点
    dummy_node = Node()
    temp_p = dummy_node
    # 比较list1和list2两个指针
    # 将值较小的节点接到p指针
    while list1 and list2:
        if list1.val > list2.val:
            temp_p.next = list2
            list2 = list2.next
        else:
            temp_p.next = list1
            list1 = list1.next
        # p指针不断前进
        temp_p = temp_p.next
        
    if list1:
        temp_p.next = list1
    if list2:
        temp_p.next = list2
    # 返回头节点
    return dummy_node.next

# 23. 合并K个升序链表
# 难点：如何快速得到k个节点中的最小节点，接到结果链表上？
# 优先队列（heapq），（基于二叉堆-最小堆，Python默认就是）自己构造HeapNode类
# 时间复杂度： O(Nlogk)，其中 k 是链表的条数，N 是这些链表的节点总数。
# 复杂度分析：优先队列heap中的元素个数最多是k，所以每一次pop和push的复杂度是logk
# 所有节点都会被加入和弹出heap一次，所以总的复杂度是n * logk
def mergeKLists(lists):
    import heapq
    heap = []
    dummy_node = Node(-1) # 虚拟头节点技巧
    pointer = dummy_node
    # 将k个链表的头节点加入最小堆
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, HeapNode(lists[i]))
    while heap:
        heap_pointer = heapq.heappop(heap).node # 获取最小节点
        pointer.next = heap_pointer        # 接到结果链表上
        if heap_pointer.next:
            heapq.heappush(heap, HeapNode(heap_pointer.next)) # 把next补充进优先队列
        # pointer指针不断前进
        pointer = pointer.next
    # 返回头节点
    return dummy_node.next

# 86.分隔链表
# 和上面一题正好相反的过程
# 具体过程：把原链表分成两个小链表，一个链表的元素大小都小于x，另一个链表的元素都大于等于x，最后再把这两条链表接到一起
# 虚拟头节点技巧
def partition(head, x):
    small_dummy_head = Node() # 存放小于x的链表虚拟头节点
    small_tmp = small_dummy_head # 负责小结果链表生成
    big_dummy_head = Node() # 存放大于等于x的链表虚拟头节点
    big_tmp = big_dummy_head # 负责大结果链表生成
    temp_p = head # 遍历原链表
    while temp_p:
        if temp_p.val >= x:
            big_tmp.next = temp_p
            big_tmp = big_tmp.next
        else:
            small_tmp.next = temp_p
            small_tmp = small_tmp.next
        temp_p = temp_p.next
    # 把大链表的next置None
    big_tmp.next = None
    small_tmp.next = big_dummy_head.next # 连接两个链表
    return small_dummy_head.next

# 141.环形链表
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

# 142. 环形链表 II
# 【难】已知链表中含有环 返回环的起始位置
# 关键： 当快慢指针相遇时，让其中任何一个指针指向头节点，然后以相同速度前进，再次相遇时所在的节点位置就是环开始的位置。
# 假设快慢指针相遇时，慢指针 slow 走了 k 步，那么快指针 fast 一定走了 2k 步
# fast 一定比 slow 多走了 k 步，这多走的 k 步其实就是 fast 指针在环里转圈圈，所以 k 的值就是环长度的「整数倍」。
# 假设相遇点距环的起点的距离为 m，那么结合上图的 slow 指针，环的起点距头结点 head 的距离为 k - m，也就是说如果从 head 前进 k - m 步就能到达环起点。
# 巧的是，如果从相遇点继续前进 k - m 步，也恰好到达环起点。因为结合上图的 fast 指针，从相遇点开始走k步可以转回到相遇点，那走 k - m 步肯定就走到环起点了：
def detectCircle(node):
    slow = node
    fast = node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    # 如果fast或fast.next为空，说明链表没有环
    if not fast or not fast.next:
        return None
    slow = node
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow

# 876.链表的中间结点
# 寻找链表的中点
def findMiddle(node):
    slow, fast = node, node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

# 寻找链表的倒数第k个元素
# 无论遍历一次链表和遍历两次链表的时间复杂度都是 O(N)
def findLastKthNode(node, k):
    slow, fast = node, node
    while k >= 1:
        k -= 1
        fast = fast.next
    
    while fast:
        slow = slow.next
        fast = fast.next
    
    return slow

# 【难】19. 删除链表的倒数第N个节点
# 要删除倒数第 n 个节点，就得获得倒数第 n + 1 个节点的引用
# 虚拟头节点技巧
def removeNthFromEnd(head, n):
    dummy_node = Node(-1)
    dummy_node.next = head
    def find_from_end(dummy_node, k):
        fast_node = dummy_node
        for _ in range(k):
            fast_node = fast_node.next
        slow_node = dummy_node
        while fast_node:
            fast_node = fast_node.next
            slow_node = slow_node.next
        return slow_node
    x = find_from_end(dummy_node, n+1)
    x.next = x.next.next
    return dummy_node.next

# 160. 相交链表：判断两个链表是否相交并返回交点
# 等价于 两个链表的第一个公共节点
# naive：额外用个set记录所有节点对比，但如何只使用两个节点完成？
# 【难】要想到这个做法需要转换思路
# 关键：通过某些方式，让 p1 和 p2 能够同时到达相交节点 c1。
# 可以让 p1 遍历完链表 A 之后开始遍历链表 B，让 p2 遍历完链表 B 之后开始遍历链表 A
# 这样相当于「逻辑上」两条链表接在了一起。
# 如果这样进行拼接，就可以让 p1 和 p2 同时进入公共部分，也就是同时到达相交节点 c1
def getIntersectionNode(headA, headB):
    pointer_a = headA
    pointer_b = headB
    while pointer_a != pointer_b:
        if pointer_a:
            pointer_a = pointer_a.next
        else:
            pointer_a = headB
        if pointer_b:
            pointer_b = pointer_b.next
        else:
            pointer_b = headA
    return pointer_a

# 206. 反转链表
# （1）递归
def reverseList(self, head):
    # 链表为空或只有一个节点时，反转结果就是它自己
    if not head or not head.next:
        return head
    # 反转当前节点之后的剩余部分
    last = reverseList(head.next)
    head.next.next = head # 核心动作
    head.next = None
    return last
# （2）迭代
def reverseList2(self, head):
    prev = None
    curr = head
    nxt = head
    while curr:
        nxt = curr.next
        curr.next = prev #逐个节点反转
        prev = curr
        curr = nxt
    return prev # 返回反转后的头节点

# 反转链表前N个节点
# 重要区别1：base case 变为 n == 1，反转一个元素，就是它本身，同时要记录后驱节点。
# 重要区别2：刚才我们直接把 head.next 设置为 null，因为整个链表反转后原来的 head 变成了整个链表的最后一个节点。
# 但现在 head 节点在递归反转之后不一定是最后一个节点了，所以要记录后驱 successor（第 n + 1 个节点），反转之后将 head 连接上。
successor = None
def reverseN(head, n):
    if n == 1:
        # 记录第n+1个节点
        successor = head.next
        return head
    # 以head.NEXT为起点反转前n-1个节点
    last = reverseN(head.next, n - 1)
    head.next.next = head # 核心动作
    head.next = successor # 让反转之后的head节点和后面的节点连起来 
    return last

# 92.反转链表
# （1）给出明确left节点和right节点
def reverseBetween(left, right):
    prev = None
    curr = left
    nxt = left
    # while的终止条件加一个不等于right就行了
    while curr != right:
        nxt = curr.next
        curr.next = prev #逐个节点反转
        prev = curr
        curr = nxt
    return prev # 返回反转后的头节点


# （2）给出数字index的范围
successor = None
def _reverseN(head, n):
    if n == 1:
        global successor
        successor = head.next
        return head
    last = _reverseN(head.next, n - 1)
    head.next.next = head
    head.next = successor
    return last

def reverseBetween(head, left, right):
    if left == 1:
        return _reverseN(head, right)
    head.next = reverseBetween(head.next, left - 1, right - 1)
    return head

# 25.K个一组翻转链表
def reverse(headA, headB):
    prev = None
    curr = headA
    nxt = headA
    while curr != headB:
        nxt = curr.next
        curr.next = prev #逐个节点反转
        prev = curr
        curr = nxt
    return prev # 返回反转后的头节点
def reverseKGroup(head, k):
    if not head or not head.next:
        return head
    # 区间[A,B)包含k个待反转元素
    headA, headB = head, head
    for _ in range(k):
        if headB:
            headB = headB.next
        else:
            return head # 不足k个，不需要反转，直接返回head就行（base case）
    # 反转前k个元素
    new_head = reverse(headA, headB)
    # 递归反转后续链表并且连接起来
    headA.next = reverseKGroup(headB, k)
    return new_head

# 234.回文链表
# 判断回文链表
# 算法总体的时间复杂度 O(N)，空间复杂度 O(1)，已经是最优的了。
# 弊端：会改变原始输入（只要在最后再反转回来即可）
def isPalindrome(head):
    # Step0 定义快指针、慢指针、前向指针
    slow, fast, prev = head, head, None

    # Step1 通过双指针技巧中的快慢指针来找到链表的中点
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # slow现在指向链表中点
    # 如果fast指针没有指向null，说明链表长度为奇数，slow还要再前进一步
    if fast:
        slow = slow.next

    # Step2 从slow开始反转后面的链表
    while slow:
        tmp = slow.next
        slow.next = prev
        prev = slow
        slow = tmp

    # Step3 开始比较回文串
    while head and prev:
        if head.val != prev.val:
            return False
        head = head.next
        prev = prev.next
    return True



