def countDigitOne(n):
    cnt = 0
    for i in range(1, n+1):
        while i != 0:
            if i % 10 == 1:
                cnt += 1
            i //= 10
    return cnt

def countDigitOne2(n):
    digit, res = 1, 0
    high, cur, low = n // 10, n % 10, 0
    while high != 0 or cur != 0:
        if cur == 0: res += high * digit
        elif cur == 1: res += high * digit + low + 1
        else: res += (high + 1) * digit
        low += cur * digit
        cur = high % 10
        high //= 10
        digit *= 10
    return res
