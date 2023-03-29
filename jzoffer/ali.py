def stay_in_map_probability(n, m, i, j, x):
    dp = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(x + 1)]

    # base case 
    for r in range(n):
        for c in range(m):
            dp[0][r][c] = 1

    # core dp
    for k in range(1, x + 1):
        for r in range(n):
            for c in range(m):
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m:
                        dp[k][r][c] += dp[k - 1][nr][nc] * 0.25
                        
    return dp[x][i][j]

    

n = 100
m = 100
i = 99
j = 99
x = 2

print(stay_in_map_probability(n, m, i, j, x))