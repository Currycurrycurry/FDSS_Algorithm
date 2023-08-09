
# 我们不需要关心染色了那些行哪些列，我们只需要关心染色的行数和列数即可，然后就是两个组合数的乘积
# n: 该正方形的边长
# k: 涂色数目

def get_possible_color_plan_num(n, k):
    def C(m, n):
        ans = 1
        for i in range(1, m + 1):
            ans *= (n - i + 1)
            ans /= i
    res = 0
    for i in range(n):
        for j in range(n):
            color_num = i * n + j * n - i * j
            if color_num == k:
                res += (C(i, n) * C(j, n))
    return res


