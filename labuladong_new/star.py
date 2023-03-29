# 3
# 2 1 5
# 6 3 7

n = int(input())
starts = list(map(int, input().split(' ')))
ends = list(map(int, input().split(' ')))

# n = 3
# ss = [2, 1, 5]
# es = [6, 3, 7]

def get_most_star_time():
    # starts.sort()
    # ends.sort()
    # res = 0
    # count = 0
    # i, j = 0, 0
    # res_times = 0
    # while i < n and j < n:
    #     if starts[i] < ends[j]:
    #         res_times += (ends[j] - starts[i]) 
    #         count += 1
    #         i += 1
    #     else:
    #         res_times -= (ends[j] - starts[i]) 
    #         j += 1
    #         count -= 1
    #     res = max(res, count)
    # return str(res) + ' ' + str(res_times)
    starts = sorted([(ss[i], i) for i in range(n)])
    ends = sorted([(es[i], i) for i in range(n)])
    max_num = max(es)
    d = [0] * (max_num * 2)
    for i in range(n):
        d[starts[i][0]] += 1
        d[ends[i][0] + 1] -= 1
    res = 0
    cnt = 0
    for i in range(1, max_num * 2):
        d[i] += d[i-1]
        if d[i] > res:
            res = d[i]
            cnt = 1
        elif d[i] == res:
            cnt += 1
    return str(res) + ' ' + str(cnt)



print(get_most_star_time())