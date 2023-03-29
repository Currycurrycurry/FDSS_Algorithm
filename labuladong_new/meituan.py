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
# n = 1
# m = 7
# k = 2
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
    dp = [[0 for _ in range(m )] for _ in range(n )]
    dp[0][0] = coins[0][0]
    res = -1
    for i in range(1, m):
        pre = dp[0][i-1] - calcluate_k(0, i-1, 0, i)
        if pre < 0:
            break
        dp[0][i] = pre + coins[0][i] 
        res = max(res, dp[0][i])
    upper_res = res
    for j in range(1, n):
        pre = dp[j - 1][0] - calcluate_k(j-1, 0, j, 0)
        if pre < 0:
            return max(upper_res, res)
        dp[j][0] = pre + coins[j][0] 
        res = max(res, dp[j][0])

    # core
    for i in range(1, n):
        for j in range(1, m):
            a = dp[i-1][j]-calcluate_k(i-1, j, i, j)
            b = dp[i][j-1] - calcluate_k(i, j-1, i, j)
            if a < 0 and b < 0:
                return res
            dp[i][j] = max(dp[i-1][j]-calcluate_k(i-1, j, i, j), dp[i][j-1] - calcluate_k(i, j-1, i, j)) + coins[i][j]
            res = max(res, dp[i][j])
    print(dp)
    return res
    
print(get_most_coins(n,m,k, COINS))
