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
# 
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


# 剑指 Offer 25. 合并两个和K个排序的链表

# 剑指 Offer 26. 树的子结构

# 剑指 Offer 27. 二叉树的镜像

# 剑指 Offer 28. 对称的二叉树


# 剑指 Offer 29. 顺时针打印矩阵

# 剑指 Offer 30. 包含min函数的栈

# 剑指 Offer 31. 栈的压入、弹出序列

# 剑指 Offer 32 三题 从上到下打印二叉

# 剑指 Offer 33. 二叉搜索树的后序遍

# 剑指 Offer 34. 二叉树中和为某一

# 剑指 Offer 35. 复杂链表的复制

# 剑指 Offer 36. 二叉搜索树与双向

# 剑指 Offer 37. 序列化二叉树

# 剑指 Offer 38. 字符串的排列

# 剑指 Offer 39. 数组中出现次数超过

# 剑指 Offer 40. 最小的k个数

# 剑指 Offer 41. 数据流中的中位数

# 剑指 Offer 42. 连续子数组的最大和

# 剑指 Offer 43. 1～n 整数中 1 出现的

# 剑指 Offer 44. 数字序列中某一位的

# 剑指 Offer 46. 把数字翻译成字符串


# 剑指 Offer 47. 礼物的最大价值


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

# 55 二叉树的深度

# 56 数组中数字出现的次数

# 57 和为s的数字

# 58 翻转字符串

# 59 队列的最大值

# 60 n个骰子的点数

# 61 扑克牌中的顺子

# 62 圆圈中最后剩下的数字

# 63 股票的最大利润

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

import numpy as np
def gradient_decsent(input_data, iteration_rounds, learning_rate):
    # initialize the x 
    X = np.rand(0, 1)
    # do gd 
    for _ in range(iteration_rounds):
        for a, b in input_data: # or mini-batch 
            delta_x = np.dot(np.reverse(a), b) 
            X -= learning_rate * delta_x
    return X
    

