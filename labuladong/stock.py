# 状态机
# DP table
# 穷举框架：利用状态进行穷举
# 
# 
'''
状态转移框架
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k][0] - prices[i])
'''
'''
base case:

dp[-1][k][0] = dp[i][0][0 = 0
dp[-1][k][1] = dp[i][0][1] = -infinity
'''

def maxProfit_k_inf(prices):
    '''
    dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
    dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
    '''
    n = len(prices)
    dp_i_0 = 0
    dp_i_1 = - float('inf')
    for i in range(n):
        temp = dp_i_0
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
        dp_i_1 = max(dp_i_1, temp - prices[i])
    return dp_i_0

# 每次sell之后要等一天才能继续交易
def maxProfit_with_cool(prices):
    n = len(prices)
    dp_i_0 = 0
    dp_i_1 = - float('inf')
    dp_pre_0 = 0
    for i in range(n):
        temp = dp_i_0
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
        dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
        dp_pre_0 = temp
    return dp_i_0

# 每次交易要支付手续费
def maxProfit_with_fee(prices, fee):
    '''
    dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
    dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
    '''
    n = len(prices)
    dp_i_0 = 0
    dp_i_1 = - float('inf')
    for i in range(n):
        temp = dp_i_0
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
        dp_i_1 = max(dp_i_1, temp - prices[i] - fee)
    return dp_i_0

def maxProfit_with_k_1(prices):
    n = len(prices)
    dp = [[0] * 2 for i in range(n)]
    for i in range(n):
        if i - 1 == -1:
            dp[i][0] = 0
            dp[i][1] = -prices[i]
            continue
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp[i][1] = max(dp[i-1][1], -prices[i])
    return dp[n-1][0]

# 如何降低动态规划问题的空间复杂度？
def maxProfit_with_k_1_optimized(prices):
    n = len(prices)
    dp_i_0 = 0
    dp_i_1 = - float('inf')
    for i in range(n):
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
        dp_i_1 = max(dp_i_1, -prices[i])
    return dp_i_0

def maxProfit_k_any(max_k, prices):
    n = len(prices)
    if max_k > n // 2:
        return maxProfit_k_inf(prices)
    dp = [[0] * 2 for i in range(max_k + 1) for j in range(n)]
    # for i in range(n):
    #     for k in range(max_k, 0, -1):
    #         if i - 1 == -1:
    #             return
    pass
            


# problem 1


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def maxProfit_k_inf(prices):
            n = len(prices)
            dp_i_0 = 0
            dp_i_1 =  - float('inf')
            for i in range(n):
                tmp = dp_i_0
                dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
                dp_i_1 = max(dp_i_1, tmp - prices[i])
            return dp_i_0
        n = len(prices)
        if k > n // 2:
            return maxProfit_k_inf(prices)
        dp = [[[0 for _ in range(2)] for _ in range(k+1)] for _ in range(n)]
        for i in range(n):
            for j in range(k, 0, -1):
                if i - 1 == -1 and (j == k or j == 1):
                    dp[i][j][1] = - float('inf')
    
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        return dp[n-2][k][0]