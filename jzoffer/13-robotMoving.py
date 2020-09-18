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

print(getRobotMovingRange(5, 10, 18))