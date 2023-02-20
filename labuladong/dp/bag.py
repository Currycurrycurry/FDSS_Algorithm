# 0-1背包框架（最基本）


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
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
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
