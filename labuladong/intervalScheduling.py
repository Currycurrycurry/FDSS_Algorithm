# 对于区间问题的处理，一般来说第一步都是排序
# 相当于预处理降低后续操作难度。
def intervalSchedule(intvs):
    if len(intvs) == 0:
        return 0
    intvs.sort(key=lambda x: x[1])

    cnt = 1
    x_end = intvs[0][1]
    for i in intvs:
        start = i[0]
        if start >= x_end:
            cnt += 1
            x_end = i[1]
    return cnt

# 435 
def eraseOverlapIntervals(intervals):
    return len(intervals) - intervalSchedule(intervals)

# 452 
def findMinArrowShots(intvs):
    if len(intvs) == 0:
        return 0
    intvs.sort(key=lambda x: x[1])

    cnt = 1
    x_end = intvs[0][1]
    for i in intvs:
        start = i[0]
        if start > x_end:
            cnt += 1
            x_end = i[1]
    return cnt

