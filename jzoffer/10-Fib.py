def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

def fib2(n):
    if n == 1 or n == 2:
        return 1
    pre, cur, post = 1, 1, 2
    while n > 2:
        pre = curr
        curr = post
        post = pre + curr
        n -= 1
    return post


