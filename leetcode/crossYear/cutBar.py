import math

def cutBar(m, n):
    slice_num = 1
    cnt = 0
    while slice_num < n:
        slice_num += min(slice_num, m)
        cnt += 1
    return cnt

def f(m, n):
    x = 1
    y = 0
    while x < n:
        x += min(x, m)
        y += 1
    return y


def cutBar(m, n):
    cnt = 0
    slice_num = n
    while slice_num > 1:
        slice_num -= min(slice_num//2, m)
        cnt += 1
    return cnt

def cutBar(m, n):
    def helper(current):
        if current >= n:
            return 0
        elif current < m: 
            return 1 + helper(current * 2)
        else:
            return 1 + helper(current + m)
    return helper(1)

def cutBar(m, n):
    i = math.log(m)//math.log(2) + 1
    j = (n - pow(2, i)) // m + 1
    return i + j

print(cutBar(3, 20))
print(cutBar(5, 100))


