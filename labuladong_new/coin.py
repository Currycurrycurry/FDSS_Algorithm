s = str(input())
n, m, k = s.split(' ')
n = int(n)
k = int(k)
m = int(m)
COLORS = [[] for _ in range(n)]
for i in range(n):
    COLORS[i] = list(input())
print(COLORS)
COINS = [[] for _ in range(n)]
for i in range(n):
    COINS[i] = list(map(int, input().split(' ')))
print(COINS)
# n = 3
# m = 3
# k = 3
# COLORS = [['B', 'B', 'R', 'B', 'R', 'B', 'R']]
# COINS = [[0,3,2,4, 1, 1, 1]]
# 3 3 3

# BBR

# BRB

# RBB

# 0 1 10

# 2 10 100

# 10 100 100
def calcluate_k(a, b, c, d):
    return 0 if COLORS[a][b] == COLORS[c][d] else k

def get_most_coins(n, m, k, coins):
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    # core
    res = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            a = dp[i-1][j]-calcluate_k(i-1, j-1, i-2, j-1)
            b = dp[i][j-1] - calcluate_k(i-1, j-2, i-1, j-1)
            # if a < 0 and b < 0:
            #     return res
            dp[i][j] = max(a, b) + coins[i-1][j-1]
            # res = max(res, dp[i][j])
    # print(dp)
    return dp[-1][-1]
    
print(get_most_coins(n,m,k, COINS))
