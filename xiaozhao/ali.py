def getShortestTime(weights):
    weights = sorted(weights)
    sum_time = 0
    n = len(weights)
    while n > 3:
        less = weights[0] + 2 * weights[1] + weights[n - 1]
        less2 = 2 * weights[0] + weights[n - 2] + weights[n - 1]
        if less > less2:
            less = less2
        sum_time += less
        n -= 2
    if n == 3:
        sum_time += sum(weights[0:3])
    elif n == 2:
        sum_time += weights[1]
    else:
        sum_time += weights[0]
    return sum_time

test_num = int(input())
ans = []
for _ in range(test_num):
    nums_len = int(input())
    weights = list(map(int, input().split(' ')))
    ans.append(getShortestTime(weights))
for a in ans:
    print(a)