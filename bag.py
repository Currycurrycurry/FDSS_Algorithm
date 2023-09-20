# 0-1背包框架（最基本）
def knapsack(W: int, N: int, wt: List[int], val: List[int]) -> int:
    assert N == len(wt)
    # 初始化一个二维数组，用于存储状态
    # dp[i][j] 表示将前 i 个物品装入容量为 j 的背包中所获得的最大价值
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    # 开始进行递推
    for i in range(1, N + 1):
        for w in range(1, W + 1):
            if w - wt[i - 1] < 0:
                # 当前商品 i 的重量已经超过了 w，无法被放入当前容量为 w 的背包中，只能选择不装入背包
                dp[i][w] = dp[i - 1][w]
            else:
                # 当前商品 i 的重量小于等于当前容量 w，可以尝试将其放入背包中
                # 取最大值，考虑是将其放入之前的最优方案中还是选择不放
                dp[i][w] = max(
                    dp[i - 1][w - wt[i - 1]] + val[i - 1],
                    dp[i - 1][w]
                )
    # 返回最大价值
    return dp[N][W]

# 416. 分割等和子集
def canPartition(self, nums) -> bool:
    nums_sum = sum(nums)
    if nums_sum % 2:
        return False
    n = len(nums)
    target = nums_sum // 2
    dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]
    for i in range(n+1):
        dp[i][0] = True
    for i in range(1, n+1):
        for j in range(1, target + 1):
            if j - nums[i - 1] < 0:
                dp[i][j] = dp[i - 1][j] # # 背包容量不足，不能装入第 i 个物品
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]] # # 装入或不装入背包
    return dp[-1][-1]

# 518. 零钱兑换 II
def change(self, amount: int, coins) -> int:
    dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
    for i in range(1, len(coins) + 1):
        dp[i][0] = 1
    for i in range(1, len(coins) + 1):
        for j in range(1, amount + 1):
            if j - coins[i-1] >= 0:
                dp[i][j] = dp[i-1][j] + dp[i][j - coins[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]

# 494. 目标和
def findTargetSumWays(self, nums: List[int], target: int) -> int:
    target += sum(nums)
    if target < 0 or target % 2:
        return 0
    target //= 2

    @cache  # 记忆化搜索
    def dfs(i, c):
        if i < 0:
            return 1 if c == 0 else 0
        if c < nums[i]:
            return dfs(i - 1, c)
        return dfs(i - 1, c) + dfs(i - 1, c - nums[i])
    return dfs(len(nums) - 1, target)