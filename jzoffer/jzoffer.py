# 剑指 Offer 03. 数组中重复的数字：数组长度为n且所有数字都在0～n-1的范围内(不一定有重复)；找出【任意一个】重复数字
# 最优：时间n(每个数字最多只要交换两次就能到自己的位置)；空间1
def positionIndexSearch(nums):
    for index, num in enumerate(nums):
        if index == num:
            continue
        elif nums[num] == num:
            return num
        else:
            nums[num], nums[index] = nums[index], nums[num]
    return -1 # 没有遇到重复数字则返回-1

# 剑指 Offer 03.下 数组中重复的数字：数组长度为n+1且所有数字都在1～n的范围内(不一定有重复)；找出【任意一个】重复数字
# 最优：时间nlgn(基于二分查找的思路)；空间1
def binarySearch(nums):
    def recursion(nums, start, end):
        def count_range(nums, start, end):
            cnt = 0
            for num in nums:
                if start <= num <= end:
                    cnt += 1
            return cnt
        if start == end: 
            return start
        mid = (start + end) // 2
        if count_range(nums, start, mid) > (mid - start + 1):
            return recursion(nums, start, mid)
        if count_range(nums, mid + 1, end) > (end - mid):
            return recursion(nums, mid + 1, end)
    return recursion(nums, 1, len(nums) - 1)

# 剑指 Offer 04. 二维数组中的查找
# 起点为：右上角（左下同理）
def search2Darray(matrix, num):
    row_len = len(matrix)
    col_len = len(matrix[0])
    row_index, col_index = 0, col_len - 1
    while row_index < row_len and col_index >= 0:
        if num == matrix[row_index][col_index]:
            return row_index, col_index
        elif num < matrix[row_index][col_index]:
            col_index -= 1
        else:
            row_index += 1
    return -1


# 剑指 Offer 05. 替换空格
# 剑指 Offer 06. 从尾到头打印链表
def stackReverse(node):
    stack = []
    while node:
        stack.append(node.val)
        node = node.next
    while stack:
        print(stack.pop())

# 剑指 Offer 07. 重建二叉树
def rebuildBT(preorder, inorder):
    if not preorder or not inorder or len(preorder) != len(inorder):
        return 
    #    1
    #  2   3
    # 4 5
    # preoder: [1, 2, 4, 5, 3]
    # inorder: [4, 2, 5, 1, 3]
    root_val = preorder[0]
    root_index = inorder.index(root_val)
    root = Node(root_val)
    root.left = rebuildBT(preorder[1:1+root_index], inorder[:root_index])
    root.right = rebuildBT(preorder[1+root_index:], inorder[root_index+1:])
    return root

# 剑指 Offer 08. 二叉树的中序遍历下一个节点
# 思想: 分三大类情况讨论【模拟】，时间复杂度n 空间复杂度1
def findNextNode_inorder(root):
    next_node = root
    # 如果有右子树
    if root.right:
        tmp = root.right
        next_node = tmp # 从右子树根节点出发
        # 那么它的下一个节点就是它的右子树中的最左子节点
        while tmp.left:
            next_node = tmp.left # 一直沿着指向左子节点的指针
            tmp = tmp.left
    # 如果没有右子树
    else:
        if root.parent:
            # 如果它是父节点的左子节点
            if root.parent.left == root:
                next_node = root.parent # 那么它的下一个节点就是父节点
            # 它是父节点的右子节点: 沿着父节点parent一路遍历直到找到一个是它父节点左子节点的节点
            else:
                tmp = root.parent
                while tmp.parent.left != tmp:
                    tmp = tmp.parent
                next_node = tmp.parent # 该节点的父节点就是我们要找的下一个节点 
    return next_node

# 剑指 Offer 09. 用两个栈实现队列
# 如何从两个先进后出的栈->先进先出的队列？
# 思想：
# 添加元素：统一加进stack1
# 删除元素：当stack2非空时，stack2栈顶的元素是一开始进入队列的元素，【直接pop它】；
#         当stack2空时，把stack1的元素逐个pop并push进stack2，再【直接pop它】
class CQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def appendTail(self, value: int) -> None:
        self.stack1.append(value)
    def deleteHead(self) -> int:
        if self.stack2:
            return self.stack2.pop()
        if not self.stack1:
            return -1
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

# 剑指 Offer 09.下 用两个队列实现栈
# 如何从两个先进先出的队列->先进后出的栈？
# 思想：queue2只起到辅助作用，核心在queue1
# 添加元素：先加进queue2末端,然后把queue1的元素也都按顺序append进来，再把完成的queue2赋给queue1
# 删除元素：直接删queue1的
class MyStack:
    def __init__(self):
        import collections
        self.queue1 = collections.deque()
        self.queue2 = collections.deque()
    def push(self, x: int) -> None:
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1
    def pop(self) -> int:
        return self.queue1.popleft()
    def top(self) -> int:
        return self.queue1[0]
    def empty(self) -> bool:
        return not self.queue1

# 只用一个队列来模拟栈：
class MyStack:
    def __init__(self):
        import collections
        self.queue = collections.deque()
    def push(self, x: int) -> None:
        n = len(self.queue)
        self.queue.append(x)
        for _ in range(n):
            self.queue.append(self.queue.popleft())
    def pop(self) -> int:
        return self.queue.popleft()
    def top(self) -> int:
        return self.queue[0]
    def empty(self) -> bool:
        return not self.queue


# 剑指 Offer 10- I. 斐波那契数列
def fib2(n):
    if n == 1 or n == 2:
        return 1
    pre, cur, post = 1, 1, 2
    while n > 2:
        pre = curr
        curr = post
        post = pre + curr
        n -= 1
    return post

# 剑指 Offer 10- II. 青蛙跳台阶问题
def numWays(self, n: int) -> int:
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a % 1000000007

# 剑指 Offer 11. 旋转数组的最小数字
# 时间复杂度Olgn(二分查找)
def findMinNumTotallyRight(nums):
    def minInOrder(nums, index1, index2):
        res = nums[index1]
        for i in range(index1+1, index2+1):
            if res > nums[i]:
                res = nums[i]
        return res
    index1 = 0
    index2 = len(nums) - 1
    indexMid = index1
    while nums[index1] >= nums[index2]:
        if index2 - index1 == 1:
            indexMid = index2
            break
        indexMid = index1 + (index2 - index1) // 2
        if nums[index1] == nums[index2] and nums[indexMid] == nums[index1]:
            return minInOrder(nums, index1, index2)
        if nums[indexMid] >= nums[index1]:
            index1 = indexMid
        elif nums[indexMid] <= nums[index2]:
            index2 = indexMid
    return nums[indexMid]

# 剑指 Offer 12. 矩阵中的路径
# dfs
def exist(board, word: str) -> bool:
    row_len, col_len = len(board), len(board[0])
    visited = [[False] * col_len for _ in range(row_len)]
    def helper(x, y, index):
        if index == len(word):
            return True
        res = False
        if 0 <= x < row_len and 0 <= y < col_len and not visited[x][y] and board[x][y] == word[index]:
            visited[x][y] = True
            index += 1
            res = helper(x+1, y, index) or helper(x-1, y, index) \
            or helper(x, y+1, index) or helper(x, y-1, index)
            if not res:
                visited[x][y] = False
                index -= 1
        return res

    for row in range(row_len):
        for col in range(col_len):
            if helper(row, col, 0):
                return True
    return False

# 剑指 Offer 13. 机器人的运动范围
def getRobotMovingRange(m, n, k):
    visited = [[False] * n for _ in range(m)]
    def canEnter(row, col):
        sum_value = 0
        while row > 0:
            sum_value += (row % 10)
            row //= 10
        while col > 0:
            sum_value += (col % 10)
            col //= 10
        return sum_value <= k
    def helper(row, col):
        if 0 <= row <= m - 1 and 0 <= col <= n - 1 and canEnter(row, col) and not visited[row][col]:
            visited[row][col] = True
            return helper(row - 1, col) + helper(row + 1, col) +\
                helper(row, col - 1) + helper(row, col + 1) + 1
        return 0
    return helper(0, 0)

# 剑指 Offer 14- I. 剪绳子
def cutIron(p, n):
    if n == 0:
        return 0
    q = -float('inf')
    for i in range(n):
        q = max(q, p[i] * cutIron(p, n - i - 1))
    return q

def cutRope_dp(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    products = [0] * (n + 1)
    for i in range(5):
        products[i] = i 
    for i in range(5, n+1):
        sum = -1
        for j in range(i//2+1):
            if products[j] * products[i-j] > sum:
                sum = products[j] * products[i-j]
        products[i] = sum
    # print(products[i])

def cutRope_greedy(n):
    times_of_3 = n // 3
    remainder = n - 3 * times_of_3
    if remainder == 1:
        return pow(3, times_of_3 - 1) * 2 * 2
    else:
        return pow(3, times_of_3) * remainder
# 剑指 Offer 14- II. 剪绳子 II


# 剑指 Offer 15. 二进制中1的个数
''' 判断二进制数中1的数目 【引申为】
（1） 判断一个整数是不是2的整数次方==是不是只有首位是1
（2） 输入两个整数m和n，计算需要改变m的二进制表示中的多少位才能得到n（先异或再统计1的个数）
'''
# 【正确解法】 左移flag
def numOf1_2(n):
    flag = 1
    num_of_1 = 0
    while flag < pow(2, 32):
        if flag & n == 1:
            num_of_1 += 1
        flag <= 1
    return num_of_1

# 【正确解法】 把一个整数减去1，再和原整数做与运算，会把该整数最右边的1变成0。
def numOf1_3(n):
    cnt = 0
    while n:
        cnt += 1
        n = (n - 1) & n
    return cnt

# 剑指 Offer 16. 数值的整数次方
def myPow(x, n):
    is_positive = True if n > 0 else False
    
    def cal_postive_pow(x, n):
        if n == 1:
            return x
        if n == 0:
            return 1
        result = cal_postive_pow(x, n//2)
        result *= result
        if n % 2 == 1:
            result *= x
        return result

    if is_positive:
        return cal_postive_pow(x, n)
    else:
        return 1 / cal_postive_pow(x, -n)
    
class Solution:
    def __init__(self):
        self.base = 1337

    # 计算 a 的 k 次方然后与 base 求模的结果
    def mypow(self, a: int, k: int) -> int:
        # 对因子求模
        a %= self.base
        res = 1
        for _ in range(k):
            # 这里有乘法，是潜在的溢出点
            res = (res * a) % self.base
        return res

    def superPow(self, a: int, b: List[int]) -> int:
        if not b:
            return 1
        last = b.pop()

        part1 = self.mypow(a, last)
        part2 = self.mypow(self.superPow(a, b), 10)
        # 每次乘法都要求模
        return (part1 * part2) % self.base

# 剑指 Offer 17. 打印从1到最大的n位数
# 需要考虑【大数问题】
# 联想：字符串全排列/组合/集合问题
def printNumbers(n):
    res = []
    if n == 0:
        return []
    nums = ['' for _ in range(n)]
    def printNum(nums, index):
        if index == n:
            res.append(int(''.join(nums)))
            return None
        for i in range(0, 10):
            nums[index] = str(i)
            printNum(nums, index + 1)
    for i in range(0, 10):
        nums[0] = str(i)
        printNum(nums, 1)

    return res[1:]  

# 剑指 Offer 18. 删除链表的节点
def deleteNode(head, val):
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

# 剑指 Offer 19. 正则表达式匹配
def isMatch(self, s: str, p: str) -> bool:
    memo = dict()
    s_len = len(s)
    p_len = len(p)
    def dp(i, j):
        if (i, j) in memo.keys():
            return memo[(i, j)]
        # base case 1: s和p都匹配完全
        if j == p_len:
            return i == s_len
        # base case 2: s匹配到底，p剩余的都是*和字母的合理（可以被消掉的）组合
        if i == s_len:
            if (p_len - j) % 2 != 0:
                return False
            # 进一步判断剩余字符串是否是[字母*]的模式
            for k in range(j+1, p_len, 2):
                if p[k] != '*':
                    return False
            return True
        # core function
        res = False
        # branch 1: 匹配
        if s[i] == p[j] or p[j] == '.':
            if j < p_len - 1 and p[j + 1] == '*':
                res = dp(i, j + 2) or dp(i + 1, j) # 匹配0次或多次
            else:
                res =  dp(i + 1, j + 1) # 匹配一次
        # branch 2: 不匹配
        else:
            if j < p_len - 1 and p[j + 1] == '*':
                res = dp(i, j + 2) # 匹配0次
            else:
                res = False # 无法匹配
        memo[(i, j)] = res
        return res
    return dp(0, 0)

# 剑指 Offer 20. 表示数值的字符串
def isNumber(self, s: str) -> bool:
    import re
    return re.match(r'^[\s]*[\+-]?(\.[\d]+|[\d]+(|\.[\d]*))([Ee][\+-]?[\d]+|)?[\s]*$', s) is not None

# 剑指 Offer 21. 调整数组顺序使奇数
def exchange(nums):
    if not nums:
        return []
    left_p, right_p = 0, len(nums) - 1
    while True:
        while left_p < len(nums) and nums[left_p] % 2 == 1:
            left_p += 1
        while right_p > 0 and nums[right_p] % 2 == 0:
            right_p -= 1
        if left_p >= right_p:
            break
        nums[left_p], nums[right_p] = nums[right_p], nums[left_p]
    return nums

# 剑指 Offer 22. 链表中倒数第k个节点
def getKthFromEnd(head, k: int):
    max_step = k
    fast_node = head
    for _ in range(max_step):
        fast_node = fast_node.next
    while fast_node:
        head = head.next
        fast_node = fast_node.next
    return head
    
# 剑指 Offer 24. 反转链表
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
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
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

# 剑指 Offer 25. 合并两个和K个排序的链表
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

# 剑指 Offer 26. 树的子结构
def hasSubTree(tree1, tree2):
    if tree1 and tree2:
        if tree1.val == tree2.val:
            return hasSubTree(tree1.left, tree2.left) and hasSubTree(tree1.right, tree2.right)
        else:
            return hasSubTree(tree1.left, tree2) or hasSubTree(tree1.right, tree2)
    if not tree1 and tree2:
        return False
    return True

# 剑指 Offer 27. 二叉树的镜像
def mirrorTree(self, root: TreeNode) -> TreeNode:
    if root:
        root.left, root.right = root.right, root.left
        self.mirrorTree(root.left)
        self.mirrorTree(root.right)
        return root

# 剑指 Offer 28. 对称的二叉树
def isSymmetric(root):
    def isSym(root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        return root1.val == root2.val and isSym(root1.left, root2.right) and isSym(root1.right, root2.left)
    return isSym(root, root)


# 剑指 Offer 29. 顺时针打印矩阵
def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    if not matrix or not matrix[0]:
        return list()
    
    rows, columns = len(matrix), len(matrix[0])
    order = list()
    left, right, top, bottom = 0, columns - 1, 0, rows - 1
    while left <= right and top <= bottom:
        for column in range(left, right + 1):
            order.append(matrix[top][column])
        for row in range(top + 1, bottom + 1):
            order.append(matrix[row][right])
        if left < right and top < bottom:
            for column in range(right - 1, left, -1):
                order.append(matrix[bottom][column])
            for row in range(bottom, top, -1):
                order.append(matrix[row][left])
        left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
    return order

# 剑指 Offer 30. 包含min函数的栈
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []
    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.min_stack:
            if x < self.min_stack[-1]:
                self.min_stack.append(x)
            else:
                self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(x)
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def min(self) -> int:
        return self.min_stack[-1]


# 剑指 Offer 31. 栈的压入、弹出序列
def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    if len(pushed) != len(popped):
        return False
    push_i = 0
    pop_i = 0
    stack = []
    while push_i < len(pushed):
        if pushed[push_i] != popped[pop_i]:
            stack.append(pushed[push_i])
            push_i += 1
        else:
            stack.append(pushed[push_i])
            push_i += 1
            pop_i += 1
            stack.pop()
            while stack and stack[-1] == popped[pop_i]:
                stack.pop()
                pop_i += 1
    while pop_i < len(popped):
        if popped[pop_i] == stack[-1]:
            pop_i += 1
            stack.pop()
        else:
            return False
    return len(stack) == 0

# 剑指 Offer 32 三题 从上到下打印二叉
def levelOrder(self, root: TreeNode) -> List[int]:
    if not root:
        return []
    queue = [root]
    res = []
    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.pop(0)
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return res

# 剑指 Offer 33. 二叉搜索树的后序遍
def verifyPostorder(self, postorder: List[int]) -> bool:
        if len(postorder) <= 1:
            return True
        root = postorder[-1]
        left_index = 0
        while left_index < len(postorder) - 1:
            if postorder[left_index] < root:
                left_index += 1
            else:
                break
        right_index = left_index
        while right_index < len(postorder) - 1:
            if postorder[right_index] > root:
                right_index += 1
            else:
                return False
        return self.verifyPostorder(postorder[:left_index]) and self.verifyPostorder(postorder[left_index:right_index])

# 剑指 Offer 34. 二叉树中和为某一值的路径
def pathSum(self, root: TreeNode, sum_: int) -> List[List[int]]:
    ret = []
    if not root:
        return ret
    path = [root]
    sums = [root.val]

    def dfs(root):
        if root.left:
            path.append(root.left)
            sums.append(sums[-1] + root.left.val)
            dfs(root.left)
        if root.right:
            path.append(root.right)
            sums.append(sums[-1] + root.right.val)
            dfs(root.right)
        if not root.left and not root.right:
            if sums[-1] == sum_:
                ret.append([p.val for p in path])
        path.pop()
        sums.pop()
    
    dfs(root)
    return ret

# 剑指 Offer 35. 复杂链表的复制
def copyRandomList(self, head: 'Node') -> 'Node':
    if not head: return head
    cur = head
    while cur:
        new_node = Node(cur.val,None,None)   # 克隆新结点
        new_node.next = cur.next
        cur.next = new_node   # 克隆新结点在cur 后面
        cur = new_node.next   # 移动到下一个要克隆的点
    cur = head

    while cur:  # 链接random
        cur.next.random = cur.random.next if cur.random else None
        cur = cur.next.next

    cur_old_list = head # 将两个链表分开
    cur_new_list = head.next
    new_head = head.next
    while cur_old_list:
        cur_old_list.next = cur_old_list.next.next
        cur_new_list.next = cur_new_list.next.next if cur_new_list.next else None
        cur_old_list = cur_old_list.next
        cur_new_list = cur_new_list.next
    return new_head

# 剑指 Offer 36. 二叉搜索树与双向链表
def treeToDoublyList(self, root: 'Node') -> 'Node':
    def dfs(cur):
        if not cur: return
        dfs(cur.left) # 递归左子树
        if self.pre: # 修改节点引用
            self.pre.right, cur.left = cur, self.pre
        else: # 记录头节点
            self.head = cur
        self.pre = cur # 保存 cur
        dfs(cur.right) # 递归右子树
    
    if not root: return
    self.pre = None
    dfs(root)
    self.head.left, self.pre.right = self.pre, self.head
    return self.head

# 剑指 Offer 37. 序列化二叉树
def serialize(self, root):
    """Encodes a tree to a single string.
    
    :type root: TreeNode
    :rtype: str
    """
    if not root:
        return '[]'
    res = []
    queue = collections.deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        if node:
            queue.append(node.left)
            queue.append(node.right)
            res.append(str(node.val))
        else:
            res.append('null')
    print(res)
    return '[' + ','.join(res) + ']'


def deserialize(self, data):
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    """
    if data == '[]': return None
    res = data[1:-1].split(',')
    for i,r in enumerate(res):
        if r == 'null':
            res[i] = None
        else:
            res[i] = int(res[i])

    if len(res) == 0:
        return None
    index = 1
    root = TreeNode(res[0])
    queue = collections.deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        if res[index] != None:
            node.left = TreeNode(res[index])
            queue.append(node.left)
        index += 1
        if res[index] != None:
            node.right = TreeNode(res[index])
            queue.append(node.right)
        index += 1
    return root

# 剑指 Offer 38. 字符串的排列
class Solution:
    res = []
    #记录回溯算法的递归路径
    track = []
    # track 中的元素会被标记为 true
    used = []

    # 主函数，输入一组不重复的数字，返回它们的全排列
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.used = [False] * len(nums)
        self.backtrack(nums)
        return self.res

    # 回溯算法核心函数
    def backtrack(self, nums):
        # base case，到达叶子节点
        if len(self.track) == len(nums):
            # 收集叶子节点上的值
            self.res.append(self.track[:])
            return

        # 回溯算法标准框架
        for i in range(len(nums)):
            # 已经存在 track 中的元素，不能重复选择
            if self.used[i]:
                continue
            # 做选择
            self.used[i] = True
            self.track.append(nums[i])
            # 进入下一层回溯树
            self.backtrack(nums)
            # 取消选择
            self.track.remove(nums[i])
            self.used[i] = False

# 剑指 Offer 39. 数组中出现次数超过一半的数字
def majorityElement(self, nums: List[int]) -> int:
    counts = collections.Counter(nums)
    return max(counts.keys(), key=counts.get)

# 剑指 Offer 40. 最小的k个数
import heapq
def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
    if k == 0:
        return list()

    hp = [-x for x in arr[:k]]
    heapq.heapify(hp)
    for i in range(k, len(arr)):
        if -hp[0] > arr[i]:
            heapq.heappop(hp)
            heapq.heappush(hp, -arr[i])
    ans = [-x for x in hp]
    return ans

# 剑指 Offer 41. 数据流中的中位数
class MedianFinder:
    def __init__(self):
        self.A = [] # small heap  bigger part heapq默认是小的！
        self.B = []# big heap smaller part
    
    def add_num(self, num):
        if len(self.A) != len(self.B):
            heapq.heappush(self.A, num)
            heapq.heappush(self.B, -heapq.heappop(self.A))
        else:
            heapq.heappush(self.B, -num)
            heapq.heappush(self.A, -heapq.heappop(self.B))
    
    def find_median(self):
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0
     

# 剑指 Offer 42. 连续子数组的最大和
# 53. 最大子数组和——优化之后的DP做法
def maxSubArray(self, nums) -> int:
    dp_0, dp_1 = nums[0], 0 
    res = dp_0
    for i in range(1, len(nums)):
        dp_1 = max(nums[i], dp_0 + nums[i])
        dp_0 = dp_1
        res = max(dp_0, res)
    return res

# 剑指 Offer 43. 1～n 整数中 1 出现的
def countDigitOne(self, n: int) -> int:
    digit, res = 1, 0
    high, cur, low = n // 10, n % 10, 0
    while high != 0 or cur != 0:
        if cur == 0: res += high * digit
        elif cur == 1: res += high * digit + low + 1
        else: res += (high + 1) * digit
        low += cur * digit
        cur = high % 10
        high //= 10
        digit *= 10
    return res
# 剑指 Offer 44. 数字序列中某一位的
def findNthDigit(self, n: int) -> int:
    start, digit, cnt = 1, 1, 9
    while n - cnt > 0:
        n -= cnt
        start *= 10
        digit += 1
        cnt = 9 * start * digit
    num = start + (n - 1) // digit
    return int(str(num)[(n-1) % digit])

# 剑指 Offer 46. 把数字翻译成字符串


# 剑指 Offer 47. 礼物的最大价值
def maxValue(grid) -> int:
    m, n = len(grid), len(grid[0])
    val = [([0] * (n + 1)) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            val[i][j] = max(val[i - 1][j], val[i][j - 1]) + grid[i - 1][j - 1]
    return val[m][n]

# 剑指 Offer 48. 最长不含重复字符的
def lengthOfLongestSubstring(self, s: str) -> int:
    if len(s) <= 1:
        return len(s)
    left, right = 0, 0
    max_len = 0
    while right < len(s) - 1:
        right += 1
        while s[right] in s[left:right]:
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

# 剑指 Offer 49. 丑数
def nthUglyNumber(n):
    dp = [0] * n
    dp[0] = 1
    p2 = p3 = p5 = 0

    for i in range(1, n):
        num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
        dp[i] = min(num2, num3, num5)
        if dp[i] == num2:
            p2 += 1
        if dp[i] == num3:
            p3 += 1
        if dp[i] == num5:
            p5 += 1       
    return dp[n-1]

# 剑指 Offer 50. 第一个只出现一次的字符
def firstUniqChar(s: str) -> str:
    tmp = dict()
    for i in s:
        if i in tmp:
            tmp[i] += 1
        else:
            tmp[i] = 1
    for t in tmp.keys():
        if tmp[t] == 1:
            return t
    return ' '

# 剑指 Offer 51. 数组中的逆序对
def mergeSort(self, nums, tmp, l, r):
    if l >= r:
        return 0

    mid = (l + r) // 2
    inv_count = self.mergeSort(nums, tmp, l, mid) + self.mergeSort(nums, tmp, mid + 1, r)
    i, j, pos = l, mid + 1, l
    while i <= mid and j <= r:
        if nums[i] <= nums[j]:
            tmp[pos] = nums[i]
            i += 1
            inv_count += (j - (mid + 1))
        else:
            tmp[pos] = nums[j]
            j += 1
        pos += 1
    for k in range(i, mid + 1):
        tmp[pos] = nums[k]
        inv_count += (j - (mid + 1))
        pos += 1
    for k in range(j, r + 1):
        tmp[pos] = nums[k]
        pos += 1
    nums[l:r+1] = tmp[l:r+1]
    return inv_count

def reversePairs(self, nums: List[int]) -> int:
    n = len(nums)
    tmp = [0] * n
    return self.mergeSort(nums, tmp, 0, n - 1)

# 剑指 Offer 52. 两个链表的第一个公共节点
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

# 剑指 Offer 53 - II. 0～n-1中缺失的数字
def missingNumber(self, nums: List[int]) -> int:
    i, j = 0, len(nums) - 1
    while i <= j:
        m = (i + j) // 2
        if nums[m] == m: i = m + 1
        else: j = m - 1
    return i

# 54 二叉搜索树的第K大节点
def kthLargest(self, root: TreeNode, k: int) -> int:
    def dfs(root):
        if not root: return
        dfs(root.right)
        if self.k == 0: return
        self.k -= 1
        if self.k == 0: self.res = root.val
        dfs(root.left)

    self.k = k
    dfs(root)
    return self.res

# 55 二叉树的深度
def maxDepth(root):
    return 1 + max(maxDepth(root.left), maxDepth(root.right)) if root else 0

# 56 数组中数字出现的次数
def singleNumbers(self, nums: List[int]) -> List[int]:
    ret = functools.reduce(lambda x, y: x ^ y, nums)
    div = 1
    while div & ret == 0:
        div <<= 1
    a, b = 0, 0
    for n in nums:
        if n & div:
            a ^= n
        else:
            b ^= n
    return [a, b]

# 57 和为s的数字
def twoSum(self, nums: List[int], target: int) -> List[int]:
    left_pointer, right_pointer = 0, len(nums) - 1
    while left_pointer < right_pointer:
        sum_value = nums[left_pointer] + nums[right_pointer]
        if sum_value < target:
            left_pointer += 1
        elif sum_value > target:
            right_pointer -= 1
        else:
            return [nums[left_pointer], nums[right_pointer]] 

# 58 翻转字符串

# 59 队列的最大值
class MaxQueue:

    def __init__(self):
        self.max_queue = collections.deque()
        self.window = collections.deque()

    def max_value(self) -> int:
        if len(self.max_queue) == 0:
            return -1
        return self.max_queue[0]

    def push_back(self, value: int) -> None:
        while self.max_queue and value > self.max_queue[-1]:
            self.max_queue.pop()
        self.window.append(value)
        self.max_queue.append(value)

    def pop_front(self) -> int:
        if len(self.window) == 0:
            return -1
        val = self.window[0]
        if val == self.max_queue[0]:
            self.max_queue.popleft()
        return self.window.popleft()


# 60 n个骰子的点数
def dicesProbability(self, n: int) -> List[float]:
    dp = [1 / 6] * 6
    for i in range(2, n + 1):
        tmp = [0] * (5 * i + 1)
        for j in range(len(dp)):
            for k in range(6):
                tmp[j + k] += dp[j] / 6
        dp = tmp
    return dp

# 61 扑克牌中的顺子
def isStraight(self, numbers: List[int]) -> bool:
    if not numbers or len(numbers) != 5:
        return False
    numbers.sort()
    zero_num = 0
    pre_num = 0
    for index, value in enumerate(numbers):
        if value == 0:
            zero_num += 1
        elif pre_num == value:
            return False
        else:
            pre_num = value
    for i in range(zero_num + 1, len(numbers)):
        if (numbers[i] - numbers[i - 1]) > zero_num + 1:
            return False
    return True

# 62 圆圈中最后剩下的数字
def lastRemaining(self, n: int, m: int) -> int:
    # return 0 if n == 1 else (self.lastRemaining(n - 1, m) + m) % n
    last = 0
    for i in range(2, n+1):
        last = (last + m) % i;
    return last

# 63 股票的最大利润
def maxProfit(self, prices: List[int]) -> int:
    cost, profit = float("+inf"), 0
    for price in prices:
        cost = min(cost, price)
        profit = max(profit, price - cost)
    return profit


# 64 求1+2+……+n

# 65 不用加减乘除做加法

# 66 构建乘积数组


# 67 字符串转换为整数
def str2int(s):
    is_positive = True
    if s[0] == '-':
        is_positive = False
        num = int(s[1:])
    elif s[0] == '+':
        num = int(s[1:])
    else:
        num = int(s)
    if not is_positive:
        return -num
    return num

# 68 树中两个节点的最低公共祖先LCA
def findLowestCommonAncester(root, node1, node2):
    def findTreePath(root, node, path=[]):
        path = path + [root]
        if root == node:
            return path
        if root.left and root.left not in path:
            return findTreePath(root.left, node, path)
        if root.right and root.right not in path:
            return findTreePath(root.right, node, path)
    path1 = findTreePath(root, node1)
    for i in path1:
        print(i.val)
    path2 = findTreePath(root, node2)
    for i in path2:
        print(i.val)
    length = min(len(path1), len(path2))
    for i in range(length):
        if path1[i] == path2[i]:
            continue 
        else:
            return path1[i-1].val
    return path1[length - 1].val





#在某2D游戏中，有一个长宽分别为n，m格的长方形栅格地图，游戏玩家起始位置在第i行，第j列的格子里，
#每一步会在上下左右四个方向中随机选择一个方向，走一步。
#求解：玩家走了x步之后，全程没有超出地图范围的概率是多少？
#注：实现函数计算上述问题，n，m，i，j，x等作为函数输入参数。


# 全局res = 0 最终：玩家走了x步之后，超出了矩形范围的路径的数量 -> p = 1 - （res/(4^^x)）


# dfs(i, j, 0)  -> dfs(i, j - 1, 1) + dfs(i, j + 1, 1) + dfs(i - 1, j, 1) + dfs(i + 1, j , 1) 
# matrix = [[0 for _ in range(m)] for _ in range(n)]
# X = 5

def get_p(m, n, X, i, j):
    res = 0
    def dfs(i, j, k):
        if k < X:
            return
        # x <= k:
        if i < 0 or i >= n or j < 0 or j >= m:
            res += 4**(X - k)
            return 
        dfs(i, j - 1, k + 1)
        dfs(i, j + 1, k + 1)
        dfs(i - 1, j, k + 1)
        dfs(i + 1, j , k + 1)
    dfs(i, j, 0)
    return 1 - (res // (4 ** X))

    
# 4 ** P
# P = X - max((i, j)到四条边的最大值)）

def stay_in_map_probability(n, m, i, j, x):
    dp = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(x + 1)]
    dp[0][i][j] = 1

    for k in range(1, x + 1):
        for r in range(n):
            for c in range(m):
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m:
                        dp[k][r][c] += dp[k - 1][nr][nc] * 0.25

    return dp[x][i][j]

n = 3
m = 3
i = 1
j = 1
x = 2

print(stay_in_map_probability(n, m, i, j, x))


# 用梯度下降法求 ax + b = 0

# ax + b = Y
# Loss function: argmin(a, b) (Y - y)^2 -> make the (ax+b)^2 min
# Get x's gradient: from 2(ax+b) = 0  get delta_x = -a^(-1)b
# update: x -= lambda(learning_rate) * delta_x

# Gradient Decsent: 
# input: {(a_n, b_n)}
# output: the best x to fit the distribution


    

def leastInterval(self, tasks: List[str], n: int) -> int:
    counter = collections.Counter(tasks)
    print(counter)
    _, max_value = max(counter.items(), key=lambda x: x[1])
    print(max_value)
    max_diff_cnt = list(counter.values()).count(max_value)
    print(max_diff_cnt)
    length = (max_value - 1) * (n + 1) + max_diff_cnt
    return length if length > len(tasks) else len(tasks)