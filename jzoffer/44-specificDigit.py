def findNthDigit(n):
    start, digit, cnt = 1, 1, 9
    while n - cnt > 0:
        n -= cnt
        start *= 10
        digit += 1
        cnt = 9 * start * digit
    num = start + (n - 1) // digit
    return int(str(num)[(n-1) % digit])