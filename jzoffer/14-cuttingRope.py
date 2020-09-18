# 自顶向下递归全整理
def cutRope_recursion(n):
    '''
        @param n: length of rope
    '''
    if n == 1:
        return n
    else:
        max_value = -float('inf')
        for i in range(1, n//2+1):
            tmp_value = max(n, cutRope_recursion(n-i) * cutRope_recursion(i))
            if max_value < tmp_value:
                max_value = tmp_value
        return max_value

print(cutRope_recursion(8))

def cutIron(p, n):
    if n == 0:
        return 0
    q = -float('inf')
    for i in range(n):
        q = max(q, p[i] + cutIron(p, n - i - 1))
    return q

def cutRope_dp(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    products = [0] * (n + 1)
    for i in range(5):
        products[i] = i 
    for i in range(5, n+1):
        sum = -1
        for j in range(i//2+1):
            if products[j] * products[i-j] > sum:
                sum = products[j] * products[i-j]
        products[i] = sum
    # print(products[i])

def cutRope_greedy(n):
    times_of_3 = n // 3
    remainder = n - 3 * times_of_3
    if remainder == 1:
        return pow(3, times_of_3 - 1) * 2 * 2
    else:
        return pow(3, times_of_3) * remainder


    





