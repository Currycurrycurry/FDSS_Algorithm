'''套路：
最优子结构并不是动态规划独有的一种性质，能求最值的问题大部分都具有这个性质；
但反之最优子结构性质作为动态规划问题的必要条件，一定是需要求最值的。
恶心人的最值题——动态规划
符合最优子结构，但不一定能够用动态规划，因为没有重叠子问题！

【1】带备忘录的递归解法的效率已经和迭代的动态规划解法一样
【2】前者是「自顶向下」进行「递归」求解，后者是「自底向上」进行「递推」求解

'''

# N叉树遍历问题
#################### 经典找零钱问题 ####################
# 最优子结构：子问题之间互相独立、互不干扰
# 要符合「最优子结构」，子问题间必须互相独立
# 为什么符合最优子结构？“因为【硬币的数量是没有限制的】，所以子问题之间没有相互制，是互相独立的。”
# （1）不带备忘录自顶向下的递归
def coinChange(coins, amount):
    def dp(n):
        if n == 0:
            return 0
        if n < 0:
            return -1
        res = float('inf')
        for coin in coins:
            subproblem = dp(n - coin)
            if subproblem == -1:
                continue
            res = min(res, 1 + subproblem)
        return res if res != float('inf') else -1
    return dp(amount)

# （2）带备忘录自顶向下的递归
def coinChange2(coins, amount):
    memos = dict()
    def dp(n):
        if n in memos:
            return memos[n]
        if n == 0:
            return 0
        if n < 0:
            return -1
        res = float('inf')
        for coin in coins:
            subproblem = dp(n - coin)
            if subproblem == -1:
                continue
            res = min(res, 1 + subproblem)
        memos[n] = res if res != float('inf') else -1
        return memos[n]
    return dp(amount)

# （3）DP一把梭！
def coinChange3(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for i in range(len(dp)):
        for coin in coins:
            if (i - coin) < 0:
                continue
            dp[i] = min(dp[i], 1 + dp[i - coin])
    return dp[amount] if dp[amount] != amount + 1 else -1


#################### 经典回溯N皇后问题 ####################
res = []
def backtrack(nums, track):
    if len(track) == len(nums):
        global res
        res.append(track)
        return
    
    for num in nums:
        if num in track:
            continue
        track.append(num)
        backtrack(nums, track)
        track.pop(-1)

#################### 经典Fib数列问题 ####################
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

def fib2(n):
    nums = [1, 1]
    for i in range(2, n):
        nums = nums[i-1] + nums[i-2]
    return nums[i-1]

def fib3(n):
    if n < 1:
        return 0
    memos = [0] * (n+1)
    return helper(memos, n)

def helper(memos, n):
    if n == 1 or n == 2:
        return 1
    if memos[n] != 0:
        return memos[n]
    memos[n] = helper(memos, n-1) + helper(memos, n-2)
    return memos[n]

# the best method: space conplexity is O(1)
def fib(n):
    if n == 2 or n == 1:
        return 1
    prev,curr = 1, 1
    for i in range(3, n+1):
        sum = prev + curr
        prev = curr
        curr = sum
    return curr


#################### 经典编辑距离问题 ####################
# 【注意】：既然每个 dp[i][j] 只和它附近的三个状态有关，
# 空间复杂度是可以压缩成 O(min(M, N)) 的（M，N 是两个字符串的长度）。
# 不难，但是可解释性大大降低
# s1 -> s2
def minDistance(s1, s2):
    def dp(i, j):
        if i == -1:
            return j + 1
        if j == -1:
            return i + 1
        
        if s1[i] == s2[j]:
            return dp(i - 1, j - 1)
        else:
            return min(
                dp(i, j - 1) + 1, # 插入
                dp(i - 1, j) + 1, # 删除
                dp(i - 1, j - 1) + 1 # 替换
            )
    return dp(len(s1) - 1, len(s2) - 1)


def minDistance_memo(s1, s2):
    memo = dict()
    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == -1:
            memo[(i, j)] = j + 1
        if j == -1:
            memo[(i, j)] = i + 1
        if s1[i] == s2[j]:
            memo[(i, j)] = dp(i-1, j-1)
        else:
            memo[(i, j)] = min(
                dp(i, j - 1) + 1, # 插入
                dp(i - 1, j) + 1, # 删除
                dp(i - 1, j - 1) + 1 # 替换
            )
        return memo[(i, j)]

def minDistance_dp(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(m):
        dp[i+1][0] = i+1
    for j in range(n):
        dp[0][j+1] = j+1
    for i in range(1, m+1, 1):
        for j in range(1, n+1, 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1, 
                    dp[i][j - 1] + 1,
                    dp[i - 1][j - 1] + 1
                )
    return dp[m][n]

class TableNode:
    def __init__(self, val):
        self.val = val 
        self.choice = 0
        # 0: none
        # 1: insert
        # 2: delete
        # 3: replace

# 降低空间复杂度
def minDistance_space(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[TableNode(0)] * (n + 1) for i in range(m + 1)]
    for i in range(m):
        dp[i+1][0].val = i+1
        dp[i+1][0].choice = 2
    for j in range(n):
        dp[0][j+1].val = j+1
        dp[0][j+1].choice = 2
    for i in range(1, m+1, 1):
        for j in range(1, n+1, 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j].val = dp[i - 1][j - 1].val
                dp[i][j].choice = 0
            else:
                dp[i][j].val = min(
                    dp[i - 1][j].val + 1,
                    dp[i][j - 1].val + 1,
                    dp[i - 1][j - 1].val + 1
                )
                if dp[i][j].val == dp[i - 1][j].val + 1:
                    dp[i][j].choice = 2
                elif dp[i][j].val == dp[i][j - 1].val + 1:
                    dp[i][j].choice = 1
                elif dp[i][j].val == dp[i-1][j-1].val + 1:
                    dp[i - 1][j - 1].choice = 3
    return dp[m][n]

def getPath(dp, m, n):
    ans = []
    while m >= 0 and n >= 0:
        tmp_choice = dp[m][n].choice
        if tmp_choice == 0:
            m -= 1
            n -= 1
        elif tmp_choice == 1:
            n -= 1
        elif tmp_choice == 2:
            m -= 1
        elif tmp_choice == 3:
            m -= 1
            n -= 1
        ans.append(tmp_choice)
    return reversed(ans)


# 300. 最长递增子序列LIS
def lengthOfLIS(nums) -> int:
    dp = [1 for _ in range(len(nums))]
    res = 0
    for i, num in enumerate(nums):
        for j in range(i):
            if nums[j] < num:
                dp[i] = max(dp[i], dp[j] + 1)   
    return max(dp)

# 354. 俄罗斯套娃信封问题——二维复杂版的最长递增子序列LIS
def maxEnvelopes(envelopes) -> int:
    if not envelopes:
        return 0  
    n = len(envelopes)
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    f = [1] * n
    for i in range(n):
        for j in range(i):
            if envelopes[j][1] < envelopes[i][1]:
                f[i] = max(f[i], f[j] + 1)
    return max(f)

# 1143. 最长公共子序列LCS
def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    text1_len = len(text1)
    text2_len = len(text2)
    dp = [[0 for _ in range(text1_len+1)] for _ in range(text2_len+1)]
    for i in range(1, text2_len+1):
        for j in range(1, text1_len+1):
            if text1[j-1] == text2[i-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]

# 583. 两个字符串的删除操作——和LCS的做法一模一样。。
def minDistance(word1: str, word2: str) -> int:
    len_word1 = len(word1)
    len_word2 = len(word2)
    dp = [[0 for _ in range(len_word2 + 1)] for _ in range(len_word1 + 1)]
    for i in range(1, len_word1 + 1):
        for j in range(1, len_word2 + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    # print(dp)
    return len_word1 + len_word2 - 2 * dp[-1][-1]

# 712. 两个字符串的最小ASCII删除和—和LCS的做法一模一样。。
def minimumDeleteSum(s1: str, s2: str) -> int:
    s1_len = len(s1)
    s2_len = len(s2)
    max_sum = 0
    dp = [[0 for _ in range(s1_len+1)] for _ in range(s2_len+1)]
    for i in range(1, s2_len+1):
        for j in range(1, s1_len+1):
            if s1[j-1] == s2[i-1]:
                dp[i][j] = dp[i-1][j-1] + ord(s1[j-1])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            max_sum = max(max_sum, dp[i][j])
    s1_sum = sum([ord(i) for i in s1])
    s2_sum = sum([ord(i) for i in s2])
    print(dp)
    return s1_sum + s2_sum - 2 * max_sum

# 53. 最大子数组和——DP做法
def maxSubArray(nums) -> int:
    dp = [0 for _ in range(len(nums))]
    res = 0
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], dp[i-1] + nums[i])   
    return max(dp)

# 53. 最大子数组和——优化之后的DP做法
def maxSubArray(self, nums) -> int:
    dp_0, dp_1 = nums[0], 0 
    res = dp_0
    for i in range(1, len(nums)):
        dp_1 = max(nums[i], dp_0 + nums[i])
        dp_0 = dp_1
        res = max(dp_0, res)
    return res

# 53. 最大子数组和——前缀和做法（已放在前缀和preSum文件中）

# 516. 最长回文子序列
def longestPalindromeSubseq(s: str) -> int:
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(n, -1, -1):
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]

# 1312. 让字符串成为回文串的最少插入次数
def minInsertions(self, s: str) -> int:
    text1 = s
    text2 = s[::-1]
    text1_len = len(text1)
    text2_len = len(text2)
    dp = [[0 for _ in range(text1_len+1)] for _ in range(text2_len+1)]
    for i in range(1, text2_len+1):
        for j in range(1, text1_len+1):
            if text1[j-1] == text2[i-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return len(s) - dp[-1][-1]

# 931. 下降路径最小和
def minFallingPathSum(matrix) -> int:
    n = len(matrix)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        dp[0][j] = matrix[0][j]
    for i in range(1, n):
        for j in range(n):
            if j == 0:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + matrix[i][j]
            elif j == n - 1:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + matrix[i][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1]) + matrix[i][j]
    return min(dp[-1])