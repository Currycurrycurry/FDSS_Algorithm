def nthUglyNumber(self, n: int) -> int:
    dp = [0] * n
    dp[0] = 1
    p2 = p3 = p5 = 0

    for i in range(1, n):
        num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
        dp[i] = min(num2, num3, num5)
        if dp[i] == num2:
            p2 += 1
        if dp[i] == num3:
            p3 += 1
        if dp[i] == num5:
            p5 += 1       
    return dp[n-1]