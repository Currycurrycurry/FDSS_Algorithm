# Josephuse 环问题
# brute-force
def findFinalNum(circle, m):
    offset = 0
    while circle:
        circle.pop((offset + m - 1) % len(circle))
        offset = (offset + m - 1) % len(circle)
        if len(circle) == 1:
            return circle[0]
    return -1

circle = [1,2, 3]
print(findFinalNum(circle, 2))

# O(N) ？正常人想的出来这方法？dbq我智商只有10
def lastRemaining(n, m):
    if n < 1 or m < 1:
        return -1
    last = 0
    for i in range(2, n+1):
        last = (last + m) % i
    return last

print(lastRemaining(10, 5))