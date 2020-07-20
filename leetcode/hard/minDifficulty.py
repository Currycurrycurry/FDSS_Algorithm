# 求n元一次整数方程的所有解，用数组表示
# l1 + l2 + l3 = k n = 3
# 1 <= l <= k-1 

def getNKEquationSolution(k: int, n:int):
    if k <= 0:
        return []
    if n == 1:
        return [[k]]
    res = []
    for i in range(1, (k-n+2), 1):
        next_part = getNKEquationSolution(k-i, n-1)
        # print(next_part)
        for sub_ans in next_part:
            res.append([i] + sub_ans)
    return res
print(getNKEquationSolution(5, 3))

# WA dp 
def getNKE_dp(k, n):
    dp = [[0] * (n+1) for i in range(k+1)]
    for i in range(k+1):
        dp[i][1] = [[i]]
    for i in range(2, n+1, 1):
        for j in range(i, k+1, 1):
            for k in range(1, j, 1):
                if dp[k][i] != 0:
                    dp[j][i] = [j-k].extend(dp[k][i])
    return dp

print(getNKE_dp(5, 3))
    
# recursion TLE 
def minDifficulty(jobDifficulty, d: int) -> int:
    if len(jobDifficulty) < d:
        return -1
    if len(jobDifficulty) == d:
        return sum(jobDifficulty)
    all_ps = getNKEquationSolution(len(jobDifficulty), d)
    total_min_difficulty = float('inf')
    for order in all_ps:
        tmp_order = []
        cnt = 0
        tmp_total_difficulty = 0
        for index, item_num in enumerate(order):
            sub_item = []
            for i in range(item_num):
                sub_item.append(jobDifficulty[cnt])
                cnt += 1
            sub_max_val = max(sub_item)
            tmp_order.append(sub_item)
            tmp_total_difficulty += sub_max_val
        if tmp_total_difficulty < total_min_difficulty:
            total_min_difficulty = tmp_total_difficulty
    return total_min_difficulty

jobD = [380,302,102,681,863,676,243,671,651,612,162,561,394,856,601,30,6,257,921,405,716,126,158,476,889,699,668,930,139,164,641,801,480,756,797,915,275,709,161,358,461,938,914,557,121,964,315]
d = 10

# print(minDifficulty(jobD, d))

# AC 
def minDifficulty_dp(jobDifficulty, d) -> int:
    if len(jobDifficulty) < d:
        return -1
    if len(jobDifficulty) == d:
        return sum(jobDifficulty)
    dp = [[float('inf')] * (len(jobDifficulty)+1) for i in range(d+1)]
    preMax = 0
    for i in range(1, len(jobDifficulty) + 1):
        preMax = max(preMax, jobDifficulty[i-1])
        dp[1][i] = preMax
    for i in range(2, d+1):
        for j in range(i, len(jobDifficulty) + 1):
            for k in range(j-1, i-2, -1):
                one_day_max_dif = max(jobDifficulty[k:j])
                dp[i][j] = min(dp[i][j], dp[i-1][k]+one_day_max_dif)
    return dp[d][len(jobDifficulty)]

jobD = [11,111,22,222,33,333,44,444]
d = 6
print(minDifficulty_dp(jobD, d))






