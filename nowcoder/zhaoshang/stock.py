# 给定一个正整数数组，它的第 i 个元素是比特币第 i 天的价格。
# 如果你最多只允许完成一笔交易（即买入和卖出一次），设计一个算法来计算你所能获取的最大利润。
# 注意你不能在买入比特币前卖出。

def maxProfit(prices):
    n = len(prices)
    dp_i_0 = 0
    dp_i_1 = - float('inf')
    for i in range(n):
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
        dp_i_1 = max(dp_i_1, -prices[i])
    return dp_i_0

nums = list(map(int, input().split()))
print(maxProfit(nums))

