from typing import List
################### 贪心算法经典问题：【区间调度】###################
################### 【区间调度】七大问题 ###################
# 对于区间问题的处理，一般来说第一步都是【排序】作为【预处理】，降低后续操作难度。

################### 问题一： 时间管理【将尽可能多的会议安排进会议室】 ###################
# 【解决方案】：将这些会议（区间）按结束时间（【右】端点）排序，然后进行处理

# 435 无重叠区间
# count：最多的无重叠区间
# len(intervals) - count：最少需要删除的区间数目
def eraseOverlapIntervals(intervals) -> int:
    intervals.sort(key=lambda x: x[1])
    x_end = intervals[0][1]
    count = 1
    for interval in intervals:
        if interval[0] >= x_end:
            count += 1
            x_end = interval[1]
    return len(intervals) - count

# 452 用最少的箭把气球都射爆
def findMinArrowShots(points) -> int:
    points.sort(key=lambda x: x[1])
    x_end = points[0][1]
    count = 1
    for point in points:
        if point[0] > x_end:
            count += 1
            x_end = point[1]
    return count

################### 问题二： 剪视频【从短片段中尽可能少地挑出部分片段来拼接出某个长片段】 ###################
# 【解决方案】：要将这些视频片段（区间）按开始时间（【左】端点）排序，然后进行处理
# 时间复杂度 nlgn
def videoStitching(clips: List[List[int]], time: int) -> int:
    clips.sort(key=lambda x: (x[0], -x[1]))
    n = len(clips)
    res = 0
    curr_end, next_end = 0, 0
    i = 0
    while i < n and clips[i][0] <= curr_end:
        while i < n and clips[i][0] <= curr_end:
            next_end = max(next_end, clips[i][1])
            i += 1
        # clips[i][1] > curr_end
        curr_end = next_end
        res += 1
        if curr_end >= time:
            return res
    return -1


################### 问题三： 删除被覆盖区间【有些区间比较短，被其他区间完全覆盖住了，请你删除这些被覆盖的区间】 ###################
# 【解决方案】：将这些区间按【左】端点【升序】排序，如果左端点相同则按右端点【降序】排序，然后就能找到并删除那些被完全覆盖的区间了
# Q：为什么 如果左端点相同则按右端点【降序】排序？
# A：对于这两个起点相同的区间，我们需要保证长的那个区间在上面（按照终点降序），这样才会被判定为覆盖，
# 否则会被错误地判定为相交，少算一个覆盖区间。

# 1288. 删除被覆盖区间
def removeCoveredIntervals(intervals) -> int:
    intervals.sort(key=lambda x: (x[0], -x[1]))
    start, end = intervals[0]
    res = 0
    for interval in intervals[1:]:
        if start <= interval[0] and interval[1] <= end:
            res += 1
        elif interval[0] > end:
            start, end = interval
        elif end >= interval[0] and end <= interval[1]:
            end = interval[1]
    return len(intervals) - res


################### 问题四： 合并重叠区间【给你若干区间，请你将所有有重叠部分的区间进行合并】 ###################
# 【解决方案】：这个问题需要将这些区间按【左】端点排序，方便找出存在重叠的区间
# 56. 合并区间
def merge(self, intervals):
    intervals.sort(key=lambda x:x[0])
    i = 0
    ans = []
    while i < len(intervals):
        left, right = intervals[i][0], intervals[i][1]
        while i+1 < len(intervals) and left <= intervals[i+1][0] <= right:
            right = max(right, intervals[i+1][1])
            i += 1
        ans.append([left, right])
        i += 1
    return ans

################### 问题五： 区间交集问题【有两个部门同时预约了同一个会议室的若干时间段，计算会议室的冲突时段】 ###################
# 【解决方案】：需要你将这些区间按【左】端点排序
# 986. 区间列表的交集
def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    if not firstList or not secondList:
        return []
    n = len(firstList)
    m = len(secondList)
    i, j = 0, 0
    res = []
    while i < n and j < m:
        a1, a2 = firstList[i]
        b1, b2 = secondList[j]
        # 没有交集：a2 < b1 or b2 < a1
        # 有交集：a2 >= b1 and b2 >= a1
        if a2 >= b1 and b2 >= a1:
            res.append([max(a1, b1), min(a2, b2)])
        if a2 < b2:
            i += 1
        else:
            j += 1
    return res

################### 问题六： 使会议室的闲置时间最少【现在只有一个会议室，还有若干会议，如何安排会议才能使这个会议室的闲置时间最少】 ###################
# 【解决方案】：0-1 背包问题的变形



################### 问题七： 合理申请会议室【如果把每个会议的起始时间看做一个线段区间，那么题目就是让你求最多有几个重叠区间】 ###################
# 【解决方案】：基于差分数组的思想，使用【扫描线技巧】扫描线的遍历过程，就是差分数组的遍历过程
# 再使用双指针【按顺序】遍历开始数组和结束数组

# 253. 会议室 II
def min_meeting_rooms(intervals) -> int:
    n = len(intervals)
    starts = []
    ends = []
    for interval in intervals:
        starts.append(interval.start)
        ends.append(interval.end)
    starts.sort()
    ends.sort()
    res = 0
    count = 0
    i, j = 0, 0
    while i < n and j < n:
        if starts[i] < ends[j]:
            count += 1
            i += 1
        else:
            j += 1
            count -= 1
        res = max(res, count)
    return res



