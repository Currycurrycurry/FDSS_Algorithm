'''套路：
最优子结构并不是动态规划独有的一种性质，能求最值的问题大部分都具有这个性质；
但反之最优子结构性质作为动态规划问题的必要条件，一定是需要求最值的。
恶心人的最值题——动态规划
符合最优子结构，但不一定能够用动态规划，因为没有重叠子问题！
'''
# N叉树遍历问题
# 经典找零钱问题
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

def coinChange3(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for i in range(len(dp)):
        for coin in coins:
            if (i - coin) < 0:
                continue
            dp[i] = min(dp[i], 1 + dp[i - coin])
    return dp[amount] if dp[amount] != amount + 1 else -1
    
# 经典回溯N皇后问题
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

# fib
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


def dp(i, j):
    dp(i - 1, j -1)
    dp(i, j - 1)
    dp(i - 1, j)


